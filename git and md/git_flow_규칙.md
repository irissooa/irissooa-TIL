### gitflow workflow 순서

1. develop branch생성 후 develop branch를 default branch로 설정
2. 중앙 원격 저장소(origin)의 develop branch와 연결된 새로운 'develop' branch를 로컬 저장소에 연결

```bash
$ git checkout -b develop origin/develop
```

3. 새로운 기능 개발을 위해 FEATURE branch를 만든다

- 로컬 저장소에서 branch를 따고, 코드를 수정하고, 변경 내용을 커밋한다.
- 이때, ‘master’ branch에서 기능 개발을 위한 브랜치를 따는 것이 아니라, ‘develop’ branch에서 따야한다.

```bash
$ git checkout -b [branch name] develop
```

4. 커밋하기 전 최신상태를 업데이트한다

```bash
$ git pull origin develop
```

5. 로컬 저장소의 새로운 기능 브랜치를 중앙 원격 저장소(remote repository)에 푸시한다.

- 새로 만든 브랜치(feature/login branch)에 새로운 기능에 대한 내용을 커밋한다.
- 커밋을 완료했다면, 내가 작업한 내용을 포함한 브랜치(feature/login branch)를 중앙 원격 저장소에 올린다.

```bash
$ git commit -a -m "Write commit message"

# 위의 명령어는 아래의 두 명령어를 합한 것
$ git add . # 변경된 모든 파일을 스테이징 영역에 추가
$ git add [some-file] # 스테이징 영역에 some-file 추가
$ git commit -m "Write commit message" # local 작업폴더에 history 하나를 쌓는 것
```

```bash
$ git push origin [branch name]
```

6. pull request를 한다

- gitlab에서 create merge를 현재 브랜치에서 develop 브랜치로 pull request를 한다

7. 로컬저장소의 develop branch에 중앙원격저장소(origin)의 최신 내용을 가져온다

```bash
$ git checkout develop
$ git pull origin develop
```

8. 기능이 완성된 feature branch를 삭제한다.

```bash
$ git branch -d [기능브렌치]
```

9. 모든 기능 완성했을 때 배포하기

- develop branch에서 버전에 대한 기능이 모두 구현되었으면 develop branch에서 그 작업에 대한 release branch를 생성 후 이동

```bash
$ git checkout -b release-버전 develop
```

- 이렇게 release 브랜치를 만드는 순간부터 배포 사이클이 시작된다.

- release 브랜치에서는 배포를 위한 최종적인 버그 수정, 문서 추가 등 릴리스와 직접적으로 관련된 작업을 수행한다.

- 직접적으로 관련된 작업들을 제외하고는 release 브랜치에 새로운 기능을 추가로 병합(merge)하지 않는다.

- ‘release’ 브랜치에서 배포 가능한 상태가 되면(배포 준비가 완료되면),

  - 배포 가능한 상태: 새로운 기능을 포함한 상태로 모든 기능이 정상적으로 동작 하는 상태

  1. 팀이 풀 리퀘스트를 통한 코드 리뷰하는 방식을 사용한다면 release 브랜치를 그대로 중앙 원격 저장소에 올린 후 다른 팀원들의 확인을 거쳐 ‘master’와 ‘develop’ branch에 병합한다.
     1. ‘master’ 브랜치에 병합한다. (이때, 병합한 커밋에 Release 버전 태그를 부여!)
     2. 배포를 준비하는 동안 release 브랜치가 변경되었을 수 있으므로 배포 완료 후 ‘develop’ 브랜치에도 병합한다.
  2. 작업했던 release 브랜치는 삭제한다. 이때, 다음 번 배포(Release)를 위한 개발 작업은 ‘develop’ 브랜치에서 계속 진행해 나간다.

```bash
# pull request 이용하지 않는 경우(우린 이용함!)
/* release 브랜치에서 배포 가능한 상태가 되면 */
// 'master' 브랜치로 이동한다.
$ git checkout master
// 'master' 브랜치에 release-1.2 브랜치 내용을 병합(merge)한다.
# --no-ff 옵션: 위의 추가 설명 참고
$ git merge --no-ff release-1.2
// 병합한 커밋에 Release 버전 태그를 부여한다.
$ git tag -a 1.2
// 'master' 브랜치를 중앙 원격 저장소에 올린다.
$ git push origin master

/* 'release' 브랜치의 변경 사항을 'develop' 브랜치에도 적용 */
// 'develop' 브랜치로 이동한다.
$ git checkout develop
// 'develop' 브랜치에 release-1.2 브랜치 내용을 병합(merge)한다.
$ git merge --no-ff release-1.2
// 'develop' 브랜치를 중앙 원격 저장소에 올린다.
$ git push origin develop

// -d 옵션: release-1.2에 해당하는 브랜치를 삭제한다.
$ git branch -d release-1.2
```

10. 버그 수정하기 

- 배포한 버전에 긴급하게 수정을 해야 할 필요가 있을 경우, ‘master’ 브랜치에서 직접 브랜치(‘hotfix’ 브랜치)를 만들어 필요한 부분만을 수정한 후 다시 ‘master’브랜치에 병합하여 이를 배포해야 한다.

```bash
// release 브랜치(hotfix-1.2.1)를 'master' 브랜치(유일!)에서 분기
$ git checkout -b hotfix-1.2.1 master

/* ~ 문제가 되는 부분만을 빠르게 수정 ~ */
git add .
git commit -m'커밋메세지'
git push origin hotfix-1.2.1
```

- 고친 hotfix 브랜치를 master에 pull request한다
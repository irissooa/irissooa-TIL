#  TIL

[toc]

## login

1. 모바일에서 입력 시 이메일 Input의 첫 글자가 대문자가 되는 현상으로 인해 로그인 실패가 발생하지 않도록 구현

> `autocapitalize` 전역 특성은 사용자가 입력하거나 수정하는 텍스트를 자동으로 대문자로 바꾸는 방식을 제거하는 열거형 특성
>
> - `off` 또는 `none`: 대문자로 변환하지 않음 (모든 문자의 기본값 소문자)
> - `on` 또는 `sentences`: 각 문장의 첫 번째 문자는 기본값 대문자, 다른 모든 문자는 기본값 소문자
> - `words`: 각 단어의 첫 번째 문자는 기본값 대문자, 다른 모든 문자는 기본값 소문자.
> - `characters`: 모든 문자의 기본값 대문자

```html
<input type="text|email|속성값" autocapitalize="off">
```



2. 로그인 실패 시 사용자에게 실패 사유 에러메시지 노출



## Page Not Found

1. 존재하지 않는 URL요청 시 Page Not Found페이지로 이동

- `routes.js`에 아래구문 추가

> 모든 페이지들을 경로와 매칭시킨 이후, route 포함되지 않은 모든 경로(default 값)에 대해서 `NotFoundPage`로 보냄. `'*'` 의 의미는 위에서 어떤 경로와도 매칭이 되지 않은 경우 해당 경로로 이동하라는 의미로 이해하면 된다

```js
 {
        path: '*',
        component: () => import('@/views/NotFoundPage.vue'),
    },
```

- `views` > `NotFoundPage.vue`

```vue
<template>
  <div>
    Page is not found
  </div>
</template>

<script>
export default {};
</script>

<style></style>
```


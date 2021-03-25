# Web_API

> [출처](https://developer.mozilla.org/en-US/docs/Web/API/File/Using_files_from_web_applications)
>
> [input MDN](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input/file)

[toc]

## Web application의 file사용

HTML5의 DOM에 추가된 `File API`를 사용하여 이제 웹 콘텐츠에서 사용자에게 로컬 파일을 선택하도록 요청한 다음 해당 파일의 콘텐츠를 읽을 수 있습니다. 

**`File`** 인터페이스는 파일에 대한 정보를 제공하고, 웹 페이지의 JavaScript가 해당 내용에 접근할 수 있는 방법을 제공합니다.

이 선택은 HTML `<input type="file">`요소를 사용하거나 끌어서 놓는 방법 으로 수행 할 수 있습니다 .

확장 또는 기타 브라우저 크롬 코드에서 DOM File API를 사용하려면 다음을 수행 할 수 있습니다. 그러나 알아야 할 몇 가지 추가 기능이 있습니다. 

```html
<input type="file" id="input">
```

File API를 사용 하면 사용자가 선택한 파일을 나타내는 `FileList`포함 `File`객체 에 액세스 할 수 있습니다 .

```js
const selectedFile = document.getElementById('input').files[0];
```




var math = math || {} // math 네임스페이스

;(function () {
  function sum(a, b) {
    return a + b
  }
  math.sum = sum // 네이스페이스에 추가
})()
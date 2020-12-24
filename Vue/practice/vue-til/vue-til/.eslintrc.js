module.exports = {
  root: true,
  env: {
    node: true
  },
  // node modules에 깔려있는 prettier 모듈을 가져와서 이부분에 들어와있다고 생각하면된다
  extends: ["plugin:vue/essential", "eslint:recommended", "@vue/prettier"],
  parserOptions: {
    parser: "babel-eslint"
  },
  rules: {
    //error라고 하면 무조건 콘솔있으면 에러가 남
    //off는 콘솔이 있더라도 에러가 나지 않는다.
    "no-console": "off",
    //개발모드일때 콘솔이 있으면 error를 내보내고, 일반 prototype 모드면 off란 뜻!
    // "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    // "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off"

    //prettier설정에 대한 객체 [eslint의 log level,프리티어의 속성]
    "prettier/prettier": ['error', {
      singleQuote: true,
      semi: true,
      useTabs: false,
      tabWidth: 2,
      trailingComma: 'all',
      printWidth: 80,
      bracketSpacing: true,
      arrowParens: 'avoid',
    }]
  },
  parserOptions: {
    parser: "babel-eslint"
  },
  overrides: [
    {
      files: [
        "**/__tests__/*.{j,t}s?(x)",
        "**/tests/unit/**/*.spec.{j,t}s?(x)"
      ],
      env: {
        jest: true
      }
    }
  ]
};

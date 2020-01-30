module.exports = {
  root: true,
  parserOptions: {
    parser: "babel-eslint",
    sourceType: 'module'
  },
  env: {
    browser: true,
    node: true
  },
  extends: [
    'standard',
    'plugin:vue/recommended'
  ],
  // required to lint *.vue files
  plugins: [
    'html',
    'standard',
    'vue'
  ],
  // add your custom rules here
  rules: {},
  globals: {}
}

module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    'plugin:vue/recommended',
    '@vue/standard',
    '@vue/airbnb',
  ],
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',

    'import/prefer-default-export': false,
    'max-len': [
      'error', {
        'code': 120,
      },
    ],
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
};

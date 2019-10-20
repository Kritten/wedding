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

    // own vue style fix
    'vue/v-bind-style': ['error', 'longform'],
    'vue/v-on-style': ['error', 'longform'],

    'import/prefer-default-export': false,
    'max-len': [
      'error', {
        'code': 120,
      },
    ],

    'class-methods-use-this': 'off',

    'object-property-newline': ['error', { allowAllPropertiesOnSameLine: false }],

    // import fix
    'import/extensions': ['error', 'always', {
      'js': 'never',
      'vue': 'never'
    }],
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
};

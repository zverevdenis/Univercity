const countryRusCodesJson = require('../../static/images/vue-tel-input/countries_rus.json');

export const CountryRusCode = countryRusCodesJson;

export const PasswordRequirements = {
    MIN_LENGTH: 8,
    REGEXP: /[a-zA-Z]+/,
    HAS_FIGURES_REGEXP: /[0-9]/
};

export const PhoneRequirements = {
    MIN_LENGTH: 8,
    HAS_FIGURES_REGEXP: /[0-9]/
};
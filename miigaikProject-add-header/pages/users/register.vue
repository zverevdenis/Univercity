<template>
    <div class="container">
        <div class="register">
            <h2 class="entry-point__header">Регистрация</h2>
            <div
                v-if="message"
                class="entry-point__message" entry-point__message--error
            >
                {{ message }}
            </div>
            <form @submit.prevent="submit" novalidate>
                <div class="entry-point__first-name">
                    <InputText
                        v-model.lazy="form.firstName"
                        :v="$v.form.firstName"
                        :textName="'Имя'"
                        :required="true"
                        :fieldName="'firstName'"
                        :errorMessage="'Введите Ваше имя'"
                    />
                </div>
                <div class="entry-point__last-name">
                    <InputText
                        v-model.lazy="form.lastName"
                        :v="$v.form.lastName"
                        :textName="'Фамилия'"
                        :required="true"
                        :fieldName="'lastName'"
                        :errorMessage="'Введите Вашу фамилию'"
                    />
                </div>
                <div class="entry-point__middle-name">
                    <InputText
                        v-model.lazy="form.middleName"
                        :v="$v.form.middleName"
                        :textName="'Отчество'"
                        :required="false"
                        :fieldName="'middleName'"
                        :errorMessage="'Введите Ваше отчество'"
                    />
                </div>
                <div class="entry-point__birthday">
                    <InputDate
                        v-model.lazy="form.birthday"
                        :v="$v.form.birthday"
                        :textName="'День рождения'"
                        :required="false"
                        :fieldName="'birthday'"
                        :errorMessage="'Введите Ваш день рождения'"
                    />
                </div>
                <div class="entry-point__gender">
                    <h3 class="complain-modal_title">Ваш пол</h3>
                    <div class="register-input-gender">
                        <InputRadio
                            v-for="sexType in sexTypes"
                            :key="sexType.id"
                            v-model.lazy="form.gender"
                            :v="$v.form.gender"
                            :name_radio = "name_radio"
                            :required = "false"
                            :value_radio = "sexType.value"
                        >
                            {{ sexType.text }}
                        </InputRadio>
                    </div>
                </div>
                <div class="entry-point__country">
                    <InputText
                        v-model.lazy="form.country"
                        :v="$v.form.country"
                        :textName="'Страну'"
                        :required="false"
                        :fieldName="'country'"
                        :errorMessage="'Введите Вашу страну'"
                    />
                </div>
                <div class="entry-point__city">
                    <InputText
                        v-model.lazy="form.city"
                        :v="$v.form.city"
                        :textName="'Город'"
                        :required="false"
                        :fieldName="'city'"
                        :errorMessage="'Введите Ваш город'"
                    />
                </div>
                <div class="entry-point__email">
                    <InputEmail
                        v-model.lazy="form.email"
                        :v="$v.form.email"
                    />
                </div>
                <div class="entry-point__phone">
                    <InputPhone
                        v-model.lazy="form.phone"
                        :v="$v.form.phone"
                        :required="true"
                        :errorMessage="'Введите Ваш номер телефона'"
                        :countryCode="countryCode"
                    />
                </div>
                <div>
                    <InputPassword
                        v-model.lazy="form.password"
                        :v="$v.form.password"
                        :textName="'Пароль'"
                        :required="true"
                        :fieldName="'password'"
                        :errorMessage="'Введите Пароль'" />
                </div>
                <button class="entry-point__btn" type="submit">
                    Зарегистрироваться
                </button>
            </form>
        </div>

    </div>
</template>

<script>
import { getRandomIntFromZeroToTheThousand } from '@/assets/js/util.js';
import { required, email, minLength, maxLength, sameAs } from 'vuelidate/lib/validators';
import { PhoneRequirements, PasswordRequirements, CountryRusCode } from '../../assets/js/const';



import axios from '../../plugins/axios';
import InputText from '@/components/common/input-text'
import InputRadio from '@/components/common/input-radio'
import InputEmail from '@/components/common/input-email'
import InputDate from '@/components/common/input-date'
import InputPhone from '@/components/common/input-phone'
import InputPassword from '@/components/common/input-password'

export default {
    components: {
        InputText,
        InputRadio,
        InputEmail,
        InputDate,
        InputPassword,
        InputPhone,
        axios,
    },
    data() {
        return{
            form: {
                firstName: '',
                lastName: '',
                middleName: '',
                birthday: '',
                country: '',
                city: '',
                email: '',
                password: '',
                phone: '',
            },
            message: '',
            sexTypes: [
                {
                    id: 1,
                    text: 'Не выбрано',
                    value: 0,
                },
                {
                    id: 2,
                    text: 'Мужской',
                    value: 1,
                },
                {
                    id: 3,
                    text: 'Женский',
                    value: 2,
                }
            ],
            name_radio: "gender",
            countryCode: "RU",
            countryRusCodeList: CountryRusCode
        }
    },
    validations: {
        form: {
            email: {},
            firstName: { required },
            lastName: { required },
            middleName: {},
            birthday: {},
            gender: {},
            password: {},
            country: { required },
            city: { required },
            phone: {
                required,
                minLength: minLength(PhoneRequirements.MIN_LENGTH),
                maxLength: maxLength(18)
            },
        }
    },
    computed: {
        uniqueIDPrefixForTextField(inputName) {
            return `${getRandomIntFromZeroToTheThousand()}-${inputName}`;
        }
    },
    methods: {
        async submit() {

            if (this.$v.form.$pending || this.$v.form.$error) {
                return;
            }

            this.isSending = true;

            const options = {
                headers: {
                    'Content-Type': 'application/json'
                }
            };
            
            var dateBirthday = null;
            if(this.form.birthday.length > 2) {
                var [YYYY, DD, MM] = this.form.birthday.split('-')
                dateBirthday = new Date(YYYY, MM, DD).toISOString();
            }
            const userDetails = {
                firstName: this.form.firstName, 
                lastName: this.form.lastName,
                middleName: this.form.middleName,
                birthday: dateBirthday,
                email: this.form.email,
                phone: this.form.phone,
                gender: this.form.gender,
                country: this.form.country,
                city: this.form.city,
                password: this.form.password,
            };

            await this.$axios.post('http://127.0.0.1:5023/users', userDetails, options)
            .catch(err => {
                this.isSending = false;
                console.log(err);
            });
        }
    }
}
</script>
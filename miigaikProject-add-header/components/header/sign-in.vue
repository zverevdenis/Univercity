<template>
    <div class="entry-point">
        <h2 class="entry-point__header">Вход</h2>

        <div class="entry-point__message entry-point__message--error" v-if="message">
            {{ message }}
        </div>
        
        <form @submit.prevent="submit" novalidate>
            <div class="entry-point__email">
                <InputEmail
                    v-model="form.email"
                    :v="$v.form.email"
                    :errorMessage="emailErrorMessage"
                >
                    <template v-if="isRegistrationConfrimRequired" #action>
                        <div class="grt-text-input__message grt-text-input__message--persistent">
                            <button
                                type="button"
                                class="grt-text-input__password-recovery-btn"
                                @click="openSendEmailWithRegistration"
                            > Отправить письмо повторно</button>
                        </div>
                    </template>
                </InputEmail>
            </div>

            <div class="entry-point__password">
                <InputPassword
                    v-model="form.password"
                    :v="$v.form.password"
                    @onPasswordRecoveryClick="openPasswordRecovery"
                />
            </div>
            <button class="grt-btn grt-btn--filled grt-btn--block" type="submit">
                Войти
            </button>
        </form>
        <nuxt-link class="specialist-button button-sign-up-registre" :to="`/users/register`">
            Зарегистрироваться
        </nuxt-link>
    </div>
</template>

<script>
import { ModalBus } from '@/event-bus/modal-bus.js';
import { required, email } from '@/node_modules/vuelidate/lib/validators';

import InputEmail from '@/components/common/input-email';
import InputPassword from '@/components/common/input-password';

export default{
    components: {
        InputEmail,
        InputPassword
    },
    data() {
        return {
            form: {
                email: '',
                password: '',
            },
            message: '',
            emailErrorMessage: 'Введите электронную почту',
            isRegistrationConfrimRequired: false
        };
    },
    validations: {
        form: {
            email: {required, email, type: Object },
            password: { required }
        }
    },
    methods: {
        submit() {

        },
        openSignUp() {

        },
        openPasswordRecovery() {

        },
        openSendEmailWithRegistration() {

        }
    }
}
</script>

<style lang="scss">
.entry-point {
    position: relative;

    @media (min-width: 768px) {
        width: 330px;
    }
}

.entry-point__header {
    margin-bottom: 18px;

    font-weight: 600;
    font-size: 18px;
    line-height: 1.4;
    color: $text-black;

    @media (min-width: 768px) {
        margin-bottom: 24px;

        font-size: 23px;
        line-height: 1.5;
    }
}

.entry-point__email,
.entry-point__password,
.entry-point__first-name,
.entry-point__last-name{
    margin-bottom: 14px;
}

.entry-point__sign-up {
    display: block;
    width: 100%;
    margin-top: 21px;
    padding: 0;

    font-family: $main-font-family;
    text-align: center;
    font-size: 13px;
    line-height: 1.4;
    color: $blue;

    appearance: none;
    background-color: transparent;
    cursor: pointer;
}

.entry-point__message {
    font-size: 13px;
    line-height: 100%;
    color: $text-black;

    &--error {
        margin-top: -12px;
        margin-bottom: 20px;

        color: $coral;
    }
}

.grt-text-input__password-recover-btn {
    padding: 0;

    font-size: 11px;
    line-height: 1.4;
    color: $blue;
    text-decoration: none;
    text-align: left;
}

.grt-text-input__message--persistent {
    display: block;
    margin-top: 3px;
    line-height: 1.4;
}

.button-sign-up-registre {
    display: inline-block;
    flex-shrink: 0;
    margin-top: 10px;
    width: 100%;
}
</style>
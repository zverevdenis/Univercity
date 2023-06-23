<template>
    <div class="login-methods">
        <p class="login-methods__text">Залогинтесь</p>

        <button
            class="grt-btn grt-btn--filled grt-btn--block grt-btn--small login-methods__enter-btn"
            type="button"
            @click="openSignIn"
        >Войти</button>

        <nuxt-link class="grt-btn--small specialist-button button-sign-up" :to="`/users/register`">
            Зарегистрироваться
        </nuxt-link>
    </div>
</template>

<script>
import { ModalBus } from '@/event-bus/modal-bus';

import SignIn from '@/components/header/sign-in';

export default {
    methods: {
        openSignIn() {
            this.$parent.$emit('on-close');

            ModalBus.$emit('open', {
                component: SignIn
            });
        }
    }
}
</script>

<style lang="scss">
.login-methods {
    @media (min-width: $desktop-mid) {
        width: 230px;
    }
}

.login-methods__text {
    @media (min-width: $desktop-mid) {
        margin-bottom: 13px;

        font-size: 13px;
        line-height: 1.4;
        color: $text-black;
    }
}

.login-methods__enter-btn {
    margin-bottom: 10px;
}

.login-methods__sign-up-link {
    display: inline-block;
    width: 100%;
    padding: 0;

    text-decoration: none;
    text-align: center;
    vertical-align: middle;
    color: $blue;
    font-family: $main-font-family;
    line-height: 1.4;

    background-color: transparent;
    cursor: pointer;
}

.button-sign-up {
    display: inline-block;
    flex-shrink: 0;
    min-width: 60px;
    max-width: 330px;
    padding: 0px 21px 0px;
}
</style>
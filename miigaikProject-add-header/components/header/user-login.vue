<template>
    <div class="header-tool__wrapper header-tool__profile">
         <div>
            <button
                v-if="!isDesktop"
                class="header-tool"
                @click="openSignIn"
            >
                <div class="header-tool_icon">
                    <svg
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path
                            fill-rule="evenodd"
                            clip-rule="evenodd"
                            d="M7 7c0-2.763 2.238-5 5-5 2.763 0 5 2.237 5 5 0 2.762-2.237 5-5 5-2.762 0-5-2.238-5-5zm5 8.382c3.713 0 7.903 2.068 7.903 2.868v1.687H4.132v-1.93c0-.8 4.155-2.625 7.868-2.625zm0-2.132c-3.338 0-10 1.675-10 5v2.5c0 .687.563 1.25 1.25 1.25h17.5c.688 0 1.25-.563 1.25-1.25v-2.5c0-3.325-6.662-5-10-5zm0-3.481a2.778 2.778 0 100-5.555 2.778 2.778 0 000 5.555z"
                            fill="#282828"
                        >
                        </path>
                    </svg>
                </div>
                <div class="header-tool__text">
                    Профиль
                </div>
            </button>
            <button
                v-if="isDesktop"
                class="header-tool"
                @click="openDropdown"
            >
                <div class="header-tool_icon">
                    <svg
                        width="32"
                        height="32"
                        viewBox="0 0 32 32"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path
                            fill-rule="evenodd"
                            clip-rule="evenodd"
                            d="M7 7c0-2.763 2.238-5 5-5 2.763 0 5 2.237 5 5 0 2.762-2.237 5-5 5-2.762 0-5-2.238-5-5zm5 8.382c3.713 0 7.903 2.068 7.903 2.868v1.687H4.132v-1.93c0-.8 4.155-2.625 7.868-2.625zm0-2.132c-3.338 0-10 1.675-10 5v2.5c0 .687.563 1.25 1.25 1.25h17.5c.688 0 1.25-.563 1.25-1.25v-2.5c0-3.325-6.662-5-10-5zm0-3.481a2.778 2.778 0 100-5.555 2.778 2.778 0 000 5.555z"
                            fill="#282828"
                        >
                        </path>
                    </svg>
                </div>
                <div class="header-tool__text">
                    Войти
                </div>
            </button>
         </div>
         <HeaderDropdown
            v-if="isDropdownOpen"
            @on-close="closeDropdown"
         >
            <LoginMethods/>
         </HeaderDropdown>   
    </div>
</template>

<script>
import { ModalBus } from '@/event-bus/modal-bus.js'

import LoginMethods from '@/components/header/login-methods';

const HeaderDropdown = () => import('@/components/common/header-dropdown');
const SignIn = () => import('@/components/header/sign-in');
export default {
    components: {
        LoginMethods,
        HeaderDropdown
    },
    props: {
        isDesktop: Boolean
    },
    data() {
        return {
            isDropdownOpen: false,
        };
    },
    methods: {
        openDropdown() {
            this.isDropdownOpen = true;
        },
        closeDropdown() {
            this.isDropdownOpen = false;
        },
        openSignIn() {
        }
    }
}
</script>

<style lang="scss">
.header-tool__profile {
    order: 2;
    z-index: $zHeader + $zAbove;

    @media (min-width: $desktop-mid) {
        order: 0;
    }
}

.header-tool__blank {
    animation-delay: 0.25s;
}

.header-tool {
    appearance: none;
    border: none;
    background-color: transparent;
}

.header-tool__wrapper {
    position: relative;
}

.slide-fade-enter-active {
    transition: all 0.3s ease;
}

.slide-fade-leave-active {
    transition: all 0.3s ease;
}

.slide-fade-enter,
.slide-fade-leave-to {
    opacity: 0;
}
</style>
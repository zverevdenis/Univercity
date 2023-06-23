<template>
    <div class="grt-tel-input grt-text-input"
        :class="{'grt-tel-input--error': v.$error || isFieldNoDirty, 'val-vti': !v.$invalid && phone}"
    >
        <VueTelInput
            v-bind="telInputProps"
            ref="phoneInputRef"
            v-model.lazy="phone"
            :disabled="disabled"
            @focus="phoneInputFocused = true"
            @blur="vueTelInputBlur"
        >
            <template #arrow-icon>
                <div class="grt-tel-input__arrow-icon"></div>
            </template>
        </VueTelInput>

        <label
            class="grt-text-input__label"
            :class = "{
                'grt-text-input__label--focus': phone || phoneInputFocused
            }"
            :for="uniqueIDPrefix"    
        >
            Телефон*
        </label>

        <div v-show="v.$error || isFieldNoDirty" class="grt-text-input__messages">
            <div class="grt-text-input__message">{{ errorMessage }}</div>
        </div>
    </div>
</template>

<script>
import { VueTelInput } from 'vue-tel-input'
import { getRandomIntFromZeroToTheThousand } from '@/assets/js/util'

export default {
    components: {
        VueTelInput
    },
    props: {
        value: {
            type: String,
            default: ''
        },
        v: {
            type: Object,
            required: true
        },
        countryCode: {
            type: String
        },
        disabled: {
            type: Boolean,
            default: false
        },
        isFieldNoDirty: {
            type: Boolean,
            default: false
        },
        errorMessage: {
            type: String
        }
    },
    computed: {
        phone: {
            get() {
                if (this.value)
                return this.value
            },
            set(newValue) {
                this.$emit('input', newValue);
            }
        }
    },
    data() {
        return {
            telInputProps: {
                autoDefaultCountry: false,
                defaultCountry: this.countryCode,
                mode: 'international',
                styleClasses: 'grt-text-input__field',
                inputOptions: {
                    showDialCode: false,
                    required: true,
                    id: '',
                    styleClasses: 'grt-text-input__input',
                    placeholder: '',
                },
                dropdownOptions: {
                    showDialCodeInSelection: true,
                    showFlags: true,
                    showDialCodeInList: true
                },
                validCharactersOnly: true,
                maxLen: 13
            },
            phoneInputFocused: false,
            uniqueIDPrefix: '',
            phoneObj: {
                formated: '',
                valid: false,
                country: undefined,
            },
        }
    },
    created() {
        this.uniqueIDPrefix = getRandomIntFromZeroToTheThousand().toString();
        this.telInputProps.inputOptions.id = this.uniqueIDPrefix;
    },
    methods: {
        changeNumber() {
            this.triggerPhoneInput()
        },
        triggerPhoneInput() {
            this.$refs.phoneInputRef.$refs.input.focus()
            this.$refs.phoneInputRef.$refs.input.select()
            this.$refs.phoneInputRef.$refs.input.scrollIntoView({
                behaviour: 'smooth',
                block: 'center',
                inline: 'center'
            })
        },
        vueTelInputBlur() {
            this.$emit('vue-tel-input-blue')
            this.phoneInputFocused = false
            this.v.$touch()
        }
    }
}
</script>

<style lang="scss">
@import "assets/scss/vti-flags.scss";

.vti__flag {
    width: 20px;
    height: 15px;
    margin-right: 5px;
    margin-left: 5px;

    box-shadow: 0 0 1px 0 #888888;
    background-image: url("static/images/vue-tel-input/vue-tel-input-flags.jpg");
    background-repeat: no-repeat;
    background-color: #dbdbdb;
    background-position: 20px 0;
}

.vue-tel-input {
    border-radius: 3px;
    display: flex;
    text-align: left;
    height: 46px;
    border: none;
}

.vue-tel-input.disabled .dropdown,
.vue-tel-input.disabled .selection,
.vue-tel-input.disabled input {
    cursor: no-drop;
}

.vue-tel-input:focus-within {
    box-shadow: none;
    border-color: transparent;
}

.vti__dropdown {
    display: flex;
    flex-direction: column;
    align-content: center;
    justify-content: center;
    position: relative;
    padding: 7px;
    cursor: pointer;

    background-color: #fff;
    border: 1px solid #bebebe;
    border-radius: 3px;

    &:focus {
        border-color: $blue;
        outline: 0;
    }
}

.vti__dropdown.show {
    max-height: 300px;
    overflow: scroll;
}

.vti__dropdown.open,
.vti__dropdown:hover {
    background-color: #f3f3f3;
}

.vti__selection {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 84px;

    font-size: 13px;
    color: $text-black;
}

.vti__selection .vti__country-code {
    color: #666;
}

.vti__dropdown-list {
    position: absolute;
    z-index: 100;
    left: -1px;

    width: 330px;
    max-height: 200px;
    margin: 0;
    padding: 0;

    text-align: left;

    list-style:none;
    background-color: #fff;
    border: none;
    border-radius: 3px;
    box-shadow: 0 0 25px rgba(0, 0, 0, 0.25);
    overflow: hidden;
    overflow-y: scroll;

    &::-webkit-scrollbar {
        background-color: #fff;
        width: 16px;
        border-radius: 3px;
    }

    &::-webkit-scrollbar-track {
        background-color: #fff;
        border-radius: 3px;
        overflow: hidden;
    }

    &::-webkit-scrollbar-track:hover {
        background-color: #f4f4f4;
    }

    &::-webkit-scrollbar-thumb {
        background-color: #babac0;
        border-radius: 16px;
        border: 5px solid #fff;
    }

    &::-webkit-scrollbar-thumb:hover {
        background-color: #a0a0a5;
        border: 4px solid #f4f4f4;
    }

    &::-webkit-scrollbar-button {
        display: none;
    }
}

.vti__dropdown-list.below {
    top: 33px;
}

.vti__dropdown-list.above {
    top: auto;
    bottom: 100%;
}

.vti__dropdown-arrow {
    transform: scaleY(0.5);
    display: inline-block;
    color: #666666;
}

.vti__dropdown-item {
    cursor: pointer;
    padding: 11px 15px;
}

.vti__dropdown-item.highlighted {
    background-color: #f3f3f3;
}

.vti__dropdown-item.last-preferred {
    border-bottom: 1px solid #cacaca;
}

.vti__dropdown-item .vti__flag{
    display: inline-block;
    margin-right: 5px;
}

.vti__input {
    width: 100%;
    outline: none;

    margin-left: 8px;
    padding-left: 14px;

    font-family: $main-font-family;

    border: 1px solid #bebebe;
    border-radius: 3px;

    &:focus {
        border-color: $blue;
    }
}

.grt-tel-input {
    position: relative;

    .grt-text-input__label {
        left: 124px;
    }

    .grt-tel-input__label {
        left: 124px;
    }

    .grt-tel-input__arrow-icon {
        margin-left: auto;
        width: 12px;
        height: 12px;
        background-repeat: no-repeat;
        background-size: contain;
    }
}

.grt-tel-input--error {
    .vti__input,
    .brt__input:focus {
        border-color: $coral;
    }

    .vti__input::placeholder {
        color: $coral;
    }

    .grt-text-input__message {
        display: block;
    }
}

.val-vti {
    .vti__input,
    .vti__input:focus {
        border-color: $azure4;
    }
}
</style>
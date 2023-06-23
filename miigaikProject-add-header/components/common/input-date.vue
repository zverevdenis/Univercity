<template>
    <div class="grt-text-input">
        <div
            class="grt-text-input__control"
            :class="{ 'grt-text-input__control--error': this.v.$error }"
        >
            <div class="grt-text-input__slot">
                <div class="grt-text-input__field">
                    <input
                        class="grt-text-input__input"
                        :class="{ 'er-form': v.$error || isFieldNoDirty, 'val-form': !v.$invalid }"
                        type="date"
                        :disabled="disabled"
                        v-model.lazy="fieldBirthday"
                        :id="uniqueIDPrefixForBirthday"
                        required
                        @blur="v.$touch()"
                    />
                    <label
                        class="grt-text-input__label"
                        :class="{ 'grt-text-input__label--focus': textName }"
                        :for="uniqueIDPrefixForBirthday"
                    >
                        {{ textName }}<span v-if="required">""</span>
                    </label>
                </div>
            </div>
            <div class="grt-text-input__messages">
                <div class="grt-text-input__message">Укажите дату своего рождения</div>
                <slot name="action"></slot>
            </div>
        </div>
    </div>
</template>

<script>
import { getRandomIntFromZeroToTheThousand } from '@/assets/js/util';

export default {
    props:{
        value : {
            type: String,
            default: '',
        },
        v: {
            type: Object,
            required: true
        },
        textName: {
            type: String,
            required: true
        },
        fieldName: {
            type: String,
            required: true
        },
        required: {
            type: Boolean,
            default: false
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
        fieldBirthday: {
            get() {
                return this.value;
            },
            set(value) {
                this.v.$touch();
                this.$emit('input', value);
            },
        },
        uniqueIDPrefixForBirthday() {
            return `${getRandomIntFromZeroToTheThousand()}-` + this.fieldName;
        }
    }
}
</script>

<style lang="scss">
.grt-text-input__field {
    position: relative;
}

.grt-text-input__input {
    box-sizing: border-box;
    flex: 1 1 auto;
    padding: 12px 14px;
    max-width: 100%;
    min-width: 0;
    width: 100%;

    font-family: $main-font-family;
    color: #7e7e7e;
    font-size: 13px;
    line-height: 18px;

    border-radius: 4px;
    border: 1px solid;
    border-color: #bebebe;
    background-color: #ffffff;

    outline: none;

    &:focus {
        border-color: $blue;
    }

    @media (min-width: 768px) {
        padding: 14px;
    }
}

.grt-text-input__label {
    position: absolute;
    top: 12px;
    left: 15px;

    font-size: 13px;

    transform-origin: top left;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.5, 1);
    pointer-events: none;

    @media (min-width: 768px) {
        top: 24px;
    }
}

.grt-text-input__input:focus ~ .grt-text-input__label,
.grt-text-input__label--focus {
    color: #bebebe;

    transform: translateY(-10px) scale(0.85);
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.5, 1) 0s;

    @media(min-width: 768px) {
        transform: translateY(-12px) scale(0.85);
    }
}

.grt-text-input__messages {
    min-height: 18px;
    display: flex;
}

.grt-text-input__message {
    display: none;
    margin-top: 3px;
    margin-left: 15px;

    font-size: 12px;
    line-height: 1.4;
    color: $coral;
}

.grt-text-input__control--error {
    .grt-text-input-message {
        display: block;
    }

    .grt-text-input__field {
        .grt-text-input__input {
            border-color: $coral;
        }

        .grt-text-input__label {
            color: $coral;
        }
    }
}

.er-form {
    border-color: $coral;
}

.val-form {
    border-color: $azure4;
}
</style>
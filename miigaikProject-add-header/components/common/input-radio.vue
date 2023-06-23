<template>
    <label class="input-radio__control" :class="{ 'input-radio__control--error': v.$error}">
        <input
            type="radio"
            :name="name_radio"
            :required="required"
            :value="value_radio"
            v-model="text"
        />
        <span class="input-radio__control-icon"></span>
        <span class="input-radio__control-text">
            <slot></slot>
        </span>
    </label>
</template>

<script>
export default {
    props: {
        required: {
            type: Boolean
        },
        value_radio: {},
        name_radio: {
            type: String
        },
        v: {
            type: Object,
            required: false
        },
    },
    computed: {
        text: {
        get() {
            return this.value;
        },
        set(value) {
            this.v.$touch();
            this.$emit('input', value);
        }
        }
    }
}
</script>

<style lang="scss">
.input-radio__control {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-top: 20px;
    cursor: pointer;

    &:hover .input-radio__control-icon {
        background: $blue;
        transition: background ease-out 250ms;
    }

    &-text {
        position: relative;
        font-size: 14px;
        color: #000;

        @media (max-width: 768px) {
            font-size: 12px;
        }
    }

    &-icon {
        position: relative;
        height: 12px;
        width: 12px;
        margin: 0 15px 0 0;
        background: $text-grey;
        border-radius: 50%;
        transition: background ease-out 250ms;

        @media (max-width: 768px) {
            margin: 0 5px 0 0;
        }

        &::after {
            content: "";
            position: absolute;
            left: 2px;
            top: 2px;
            display: block;
            width: 8px;
            height: 8px;
            background: $white;
            border-radius: 50%;
            transform: scale(1);
            transition: transform ease-out 250ms;
        }
    }

    >input {
        position: absolute;
        z-index: -1;
        opacity: 0;

        &:checked {
            & + .input-radio__control-icon {
                background: $dark-orange;
                transition: background ease-out 250ms;

                &::after {
                    transform: scale(0.5);
                    transition: all ease-in 250ms;
                }
            }
        }
    }
}
</style>
<template>
    <footer class="footer">
        <div class="container">
            <div class="footer-wrapper">
                <Contacts />
                <div class="footer__copyright">{{ copyrightText }}</div>
            </div>
        </div>
    </footer>
</template>

<script>
import Contacts from '~/components/footer/contacts.vue'

export default {
    components: {
        Contacts
    },
    computed: {
        copyrightText() {
            const currentYear = new Date().getFullYear();
            return `@ 2023-${currentYear}, Маркетплейс`;
        }
    },
}


</script>

<style lang="scss">
.footer {
    background: linear-gradient(#b8e356, #b8e356);
}

.footer-wrapper {
    @media(min-width: $pad) {
        display: flex;
        flex-wrap: wrap;
        padding-top: 44px;
        justify-content: space-between;
    }
}

.footer__copyright{
    flex-shrink: 0;
    width: 100%;
    padding: 14px 0;
    border-top: 1px solid #e7e7e7;
    font-size: 11px;
    line-height: 1.4;
    color: #131313;

    @media (min-width: $pad) {
        text-align: center;
    }
}

.footer__subscribe {
    @media (min-width: $pad) {
        order: -2;
        width: 50%;
    }

    @media (min-width: $desktop-mid) {
        order: 0;
        width: 30%;
    }
}
</style>
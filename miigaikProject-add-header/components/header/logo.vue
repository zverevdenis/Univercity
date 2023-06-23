<template>
    <a class="header-logo" to="/">
        <picture>
            <source
                media="(min-width: 1025px)"
                srcset="/images/logo/logo-desktop.jpg"
            />
            <source
                media="(min-width: 768px)"
                srcset="/images/logo/logo-tablet.webp"
            />
            <img
                class="header-logo__image"
                src="/images/logo/logo-mobile.gif"
                alt="Title"
                width="90"
                height="22"
            />
        </picture>
    </a>
</template>

<style lang="scss" scoped>
.header-logo {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 12px 0;

    @media (min-width: 768px) {
        padding: 16px 0;
    }

    @media (min-width: $desktop-mid) {
        padding: 30px 0 30px;
    }
    
    .header-logo__image {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-shrink: 0;
        width: 90px;
        height: 22px;

        aspect-ratio: 45 / 11;

        @media (min-width: $pad) {
            width: 112px;
            height: 40px;

            aspect-ratio: 14 / 5;
        }

        @media (min-width: $desktop-mid) {
            width: 224px;
            height: 99px;

            aspect-ratio: 224 / 99;
        }
    }
}
</style>
<template>
    <div>
        <Header />
        <nuxt :key="$route.fullPath" />
        <Footer />
        <client-only>
            <Modal/>
        </client-only>
    </div>
</template>

<script>
import Header from '@/components/header/header';
import Footer from '@/components/footer/footer';
import Modal from '@/components/common/modal';

export default{
    name: "default",
    components: {
        Header,
        Footer,
        Modal
    }
    
}
</script>

<style lang="scss">
    .page-body{
        position: relative;
    }

    .page-main{
        position: relative;
        z-index: $zMain;
    }

    .page-main--above-header{
        z-index: $zAbove + $zHeader;
    }

    .user-confirm-position{
        position: fixed;
        top: 0;
        left: 0;
        z-index: 10000;
    }
</style>
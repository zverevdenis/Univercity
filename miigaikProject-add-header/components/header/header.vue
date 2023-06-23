<template>
    <header ref="header" class="header">
        <div class="header-main">
            <div class="container">
                <div class="header-row">
                <Logotype />
                <SearchBar />
                <Tools
                    v-if="fetchedUser"
                    :isDesktop="isDesktop"
                />
                </div>
            </div>
        </div>
    </header>
</template>

<script>
import Logotype from '@/components/header/logo';
import SearchBar from './search-bar.vue';

export default{
    components: {
    Logotype,
    SearchBar,
    Tools: () => import('@/components/header/tools')
    },
    data() {
        return {
            isDesktop: true,
            fetchedUser: true
        }
    }
}
</script>

<style lang="scss">

.header {
    position: relative;
    z-index: $zHeader;
    z-index: 10;
}

.header-main {
    @media (max-width: 767px) {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: $zHeader + $zAbove;
    z-index: 10 + 1;
    background-color: #ffffff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
}

.header-row {
    display: flex;
    flex-flow: row nowrap;
    justify-content: space-between;
    align-items: center;
    position: relative;
}

.page-main {
    @media (max-width: 767px) {
        padding: 42px;
    }
}
</style>
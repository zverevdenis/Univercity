<template>
    <div class="header-tools">
        <UserLoggedIn v-if="user"/>
        <UserLogin :isDesktop="isDesktop" v-else/>
    </div>
</template>

<script>
import UserLoggedIn from '@/components/header/user-logged-in';
import UserLogin from '@/components/header/user-login';

export default {
    components: {
        UserLoggedIn,
        UserLogin
    },
    props: {
        isDesktop: Boolean
    },
    data() {
        return {
            user: false
        }
    }
}
</script>
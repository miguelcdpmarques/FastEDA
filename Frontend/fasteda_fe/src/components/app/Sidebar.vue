<template>
    <nav id="sidebar">
        <div class="sidebar-header">
            <h3>Fast EDA</h3>
        </div>
        <ul class="sidebar-list-pages">
            <li class="active">
                <router-link class="nav-link" :to="{name: 'import'}">Data</router-link>
            </li>
            <li>
                <router-link class="nav-link" :to="{name: 'visualization'}">Visualization</router-link>
            </li>
        </ul>
        <div class="sidebar-account">
            <h5 class="sidebar-account-name">Miguel</h5>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'Sidebar'
}
</script>

<style>

</style>

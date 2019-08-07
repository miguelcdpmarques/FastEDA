<template>
    <div class="page-content">
        <content-title></content-title>
        <content-body></content-body>
    </div>
</template>

<script>
import ContentTitle from './ContentTitle.vue'
import ContentBody from './ContentBody.vue'

export default {
    name: 'visualization',
    components: {
        'content-body': ContentBody,
        'content-title': ContentTitle
    }
}
</script>

<style>
</style>

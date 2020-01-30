<script>
export default {
  name: 'Logout',
  mounted () {
    // this.$store
    //   .dispatch('doLogout')
    //   .then((result) => {
    //     this.$router.push({ name: 'Login' })
    //   })
    this.$cookie.delete('admin-id')
    window.location.href = '/wadmin'
  }
}
</script>

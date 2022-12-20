<template>
  <AppSidebar />
  <AppHeader />

  <v-spacer class="page">
    <v-spacer class="d-flex page box p-3">Dashboard</v-spacer>
    <v-spacer class="page content shadow p-3">
      Dashboard Content Goes Here
    </v-spacer>
  </v-spacer>
</template>

<script>
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue";

export default {
  name: "DashboardComponent",
  components: {
    AppSidebar,
    AppHeader,
  },
  data() {
    return {};
  },
};
</script>
<style>
.page {
  color: white;
  padding: 0 1rem;
  background: #f9f1f1;
}
.box {
  padding-top: 20px;
  min-height: 120px;
  background: #510f13;
  margin: 0 -1rem;
  font-size: 30px;
}
.content {
  min-height: calc(100vh - 178px);
  border-radius: none !important;
  margin-top: -2rem;
  background: white;
  color: black;
  font-size: 1rem;
  padding-top: 20px;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}
.data {
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>

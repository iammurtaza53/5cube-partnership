<template>
  <AppSidebar />
  <AppHeader />
  <div app class="page">
    <div class="d-flex page box p-3">Statistics</div>
    <div class="content page shadow p-3 position-relative">
      <v-select
        v-model="group"
        :items="groupList"
        label="Choose Group"
        item-title="name"
        item-value="id"
        required
      >
      </v-select>
      <v-btn @click="filter_data_by_groupId(group)">Filter</v-btn>
      <v-table>
    <thead>
      <tr>
        <th class="text-left">S No.#</th>
        <th class="text-left">Expense</th>
        <th class="text-left">Amount</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item, i) in filter.expense" :key="item.person">
        <td>{{ i + 1 }}.</td>
        <td>{{ item.name }}</td>
        <td>Rs {{ item.amount }}/-</td>
      </tr>
    </tbody>
  </v-table>
    </div>
  </div>
  
</template>
<script>
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue";
// import AppModal from "./AppModal.vue";
import api from "../api";

export default {
  name: "CategoryComponent",
  components: {
    AppSidebar,
    AppHeader,
  },
  mounted() {
    this.getGroup();
  },
  data() {
    return {
      group: "",
      groupList: [],
      filter: [],
    };
  },
  methods: {
    async getGroup() {
      await api.get("group_list/").then((response) => {
        this.groupList = response;
      });
    },
    async filter_data_by_groupId(id) {
      await api.get("stats_filter/" + id).then((response) => {
        this.filter = response;
        console.log(this.filter);
      });
    },
  },
};
</script>

<style scope>
/* .content {
  min-height: calc(100vh - 178px);
  border-radius: none !important;
  margin-top: 0;
  background: white;
  color: black;
  font-size: 1rem;
  padding-top: 20px;
} */
</style>

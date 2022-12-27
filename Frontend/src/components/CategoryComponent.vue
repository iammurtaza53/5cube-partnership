<!-- this is category component page is used to show the category list and to view, create, edit and delete category -->
<template>
  <!-- AppSidebar is used to show the sidebar -->
  <AppSidebar />
  <!-- AppHeader is used to show the (5cube expense Management) header -->
  <AppHeader />

  <div app class="page">
    <div class="d-flex page box p-3">Categories</div>
    <div class="content page shadow p-3 position-relative">
      <!-- app-modal component is used to show the modal to create category with type="Create" and to edit category with type="Edit" -->

      <AppModal type="Create" />
      <v-table>
        <thead>
          <tr>
            <th class="text-left">S No. #</th>
            <th class="text-left">Name</th>
            <th class="text-left">Type</th>
            <th class="text-left" width="20px">Edit</th>
            <th class="text-left" width="20px">Delete</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in category" :key="item.name">
            <td>{{ i + 1 }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.type }}</td>
            <td>
              <AppModal type="Edit" />
              <!-- <AppModal type="Edit" /> -->
            </td>
            <td>
              <v-btn outlined plain size="x-small" icon>
                <v-icon color="error">mdi-delete</v-icon>
              </v-btn>
            </td>
          </tr>
        </tbody>
      </v-table>
    </div>
  </div>

</template>
<script>
import axios from "axios";
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue";
import AppModal from "./AppModal.vue";
export default {
  name: "CategoryComponent",
  components: {
    AppSidebar,
    AppHeader,
    AppModal,
  },
  async mounted() {
    let category = await axios.get("http://127.0.0.1:8000/catinfo/");
    console.log(category.data.data);
    this.catlist = category.data.data;
  },
  data() {
    return {
      catlist:[],
      // category: [
      //   {
      //     name: "Food",
      //     type: "Expense",
      //   },
      //   {
      //     name: "Client",
      //     type: "Income",
      //   },
      //   {
      //     name: "Salary",
      //     type: "Expense",
      //   },
      //   {
      //     name: "Transport",
      //     type: "Expense",
      //   },
      //   {
      //     name: "Rent",
      //     type: "Expense",
      //   },
      //   {
      //     name: "Bills",
      //     type: "Expense",
      //   },
      //   {
      //     name: "Other",
      //     type: "Expense",
      //   },
      // ],
    };
  },
};
</script>

<style></style>

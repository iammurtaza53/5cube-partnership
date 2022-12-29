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

      <AppModal types="Create" :getCategories="getCategories"/>
      <!--  @get-categories="getCategories" -->
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
          <tr v-for="(item,i) in categoryList" :key="item.id">
            <td>{{ i+1 }}</td>
            <td>{{ item.cname }}</td>
            <td>{{ item.ctype }}</td>
            <td>
              <AppModal types="Edit" :getCategories="getCategories"/>
            </td>
            <td>
              <v-btn
                v-on:click="deleteCategories(item.id)"
                outlined
                plain
                size="x-small"
                icon
              >
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
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue";
import AppModal from "./AppModal.vue";
import axios from "axios";
export default {
  name: "CategoryComponent",
  components: {
    AppSidebar,
    AppHeader,
    AppModal,
  },

  data() {
    return {
      categoryList: [],
    };
  },
  mounted() {
    this.getCategories();
  },
  methods: {
    async getCategories() {
      let getCategoryURL = await axios.get(
        "http://127.0.0.1:8000/category_list/"
      );
      this.categoryList = getCategoryURL.data;
    },

    async deleteCategories(id) {
      console.log("deleteCategories", id);
      await axios.delete("http://127.0.0.1:8000/category_delete", {
        data: {
          id: id,
        },
      });
      this.getCategories();
    },
  },
};
</script>

<style></style>

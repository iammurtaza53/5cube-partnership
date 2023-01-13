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

      <AppModal types="Create" :isEdit="!isEdit" :getCategories="getCategories"/>
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
            <td>{{ item.name }}</td>
            <td>{{ item.type }}</td>
            <td>
              <AppModal :isEdit="isEdit" types="Edit" :category="item" :getCategories="getCategories"/>
            </td>
            <td>
              <v-btn
                v-on:click="deleteCategories(item.id)" outlined plain size="x-small" icon>
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
import api from '../api';

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
      isEdit:true,
    };
  },
  mounted() {
    this.getCategories();
  },
  methods: {
    async getCategories() {
      api.get("category_list")
      .then((response)=>{
          this.categoryList = response
      });
    },
    async deleteCategories(id) {
      api.delete("category_delete",{
        data:{
          id:id
        }
      }).then((response)=>{
        this.getCategories();
          return response.data
      })
     
    },
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


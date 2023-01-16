<!-- this is category component page is used to show the category list and to view, create, edit and delete category -->
<template>
  <!-- AppSidebar is used to show the sidebar -->
  <AppSidebar />
  <!-- AppHeader is used to show the (5cube expense Management) header -->
  <AppHeader />

  <div app class="page">
    <!-- <div class="d-flex page box p-3">Categories</div> -->
    <div class="content page shadow p-3 position-relative">
      <!-- app-modal component is used to show the modal to create category with type="Create" and to edit category with type="Edit" -->

      <AppModal
        types="Create"
        :isEdit="!isEdit"
        :getCategories="getCategories"
      />
      <!--  @get-categories="getCategories" -->
      <v-table style="width:100%">
        <thead>
          <tr>
            <th class="text-left" width="20%">S No. #</th>
            <th class="text-left" width="30%">Name</th>
            <th class="text-left" width="30%">Type</th>
            <th class="text-left" width="10%">Edit</th>
            <th class="text-left" width="10%">Delete</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in categoryList" :key="item.id">
            <td>{{ i + 1 }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.type }}</td>
            <td>
              <AppModal
                :isEdit="isEdit"
                types="Edit"
                :category="item"
                :getCategories="getCategories"
              />
            </td>
            
            <td>
              <v-menu
                v-model="dialogNote[item.id] "
                
                location="end"
              >
                <template v-slot:activator="{ props }">
                  <v-btn
                    outlined
                    plain
                    size="x-small"
                    icon
                    v-bind="props"
                  >
                    <v-icon color="error">mdi-delete</v-icon>
                  </v-btn>
                </template>
                
                <v-card min-width="300">
                  <v-list>
                    <v-list-item>
                      Delete Confirmation
                    </v-list-item>
                  </v-list>
                  <v-divider></v-divider>
                  <v-list>
                    <v-list-item>
                     Are you sure you want to delete this category?
                    </v-list-item> 
                  </v-list>

                    <v-spacer></v-spacer>
                    <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn variant="text"> Cancel </v-btn>
                    <v-btn color="primary" variant="text" @click="deleteCategories(item.id)">
                      Delete
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-menu>
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
import api from "../api";

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
      isEdit: true,
      dialogNote: {},
    };
  },
  mounted() {
    this.getCategories();
  },
  methods: {
    async getCategories() {
      api.get("category_list").then((response) => {
        this.categoryList = response;
      });
    },
    async deleteCategories(id) {
      // if (confirm("are you sure?")) {
        api
          .delete("category_delete", {
            data: {
              id: id,
            },
          })
          .then((response) => {
            this.getCategories();
            return response.data;
          });
      // }
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

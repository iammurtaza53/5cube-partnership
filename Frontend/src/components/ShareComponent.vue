<template>
  <AppSidebar />
  <AppHeader />
  <div class="page">
    <div class="d-flex page box p-3">Shares Details</div>
    <div class="page content shadow p-3 position-relative">
      <ShareModal types="Create" :isEdit="!isEdit" :getShares="getShares" />
      <v-table>
        <thead>
          <tr>
            <th class="text-left">S No.#</th>
            <th class="text-left">Person</th>
            <th class="text-left">Salary</th>
            <th class="text-left">Share</th>
            <th class="text-left" width="20px">Edit</th>
            <th class="text-left" width="20px">Delete</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in shareList" :key="item.name">
            <td>{{ i + 1 }}.</td>
            <td>{{ item.name }}</td>
            <td>Rs {{ item.salary }}/-</td>
            <td>{{ item.share }}%</td>
            <td>
              <ShareModal
                :isEdit="isEdit"
                types="Edit"
                :share="item"
                :getShares="getShares"
              />
            </td>

            <td>
              <v-menu v-model="dialogNote[item.id]" location="end">
                <template v-slot:activator="{ props }">
                  <v-btn outlined plain size="x-small" icon v-bind="props">
                    <v-icon color="error">mdi-delete</v-icon>
                  </v-btn>
                </template>

                <v-card min-width="300">
                  <v-list>
                    <v-list-item> Delete Confirmation </v-list-item>
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
                    <v-btn
                      color="primary"
                      variant="text"
                      @click="deleteShares(item.id)"
                    >
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
import api from "../api";
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue";
import ShareModal from "./ShareModal.vue";
export default {
  name: "ShareComponent",
  components: {
    AppSidebar,
    AppHeader,
    ShareModal,
  },
  data() {
    return {
      shareList: [],
      isEdit: true,
      dialogNote: {},
    };
  },
  mounted() {
    this.getShares();
  },
  methods: {
    async getShares() {
      api.get("share_list/").then((response) => {
        this.shareList = response;
      });
    },
    async deleteShares(id) {
      api
        .delete("share_delete", {
          data: {
            id: id,
          },
        })
        .then((response) => {
          this.getCategories();
          return response.data;
        });
    },
  },
};
</script>
<style></style>

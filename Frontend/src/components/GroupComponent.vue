<template>
  <AppSidebar />
  <AppHeader />
  <v-spacer class="page">
    <v-spacer class="d-flex page box p-3">Group</v-spacer>
    <v-spacer class="page content shadow p-3">
      <GroupModal types="Create" :isEdit="!isEdit" :getGroup="getGroup" />
      <v-table>
        <thead>
          <tr>
            <th class="text-left">S No. #</th>
            <th class="text-left">Name</th>
            <th class="text-left">Start Date</th>
            <th class="text-left">End Date</th>
            <th class="text-left">is_Active</th>
            <th class="text-left" width="20px">Edit</th>
            <th class="text-left" width="20px">Delete</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in groupList" :key="item.name">
            <td>{{ i + 1 }}.</td>
            <td>{{ item.name }}</td>
            <td>{{ item.start_date }}</td>
            <td>{{ item.end_date }}</td>
            <td v-if="item.isActivated"><v-btn width="50" color="success" size="x-small">{{item.isActivated}}</v-btn></td>

            <td v-if="!item.isActivated"><v-btn  color="error" size="x-small" @click="update_activation(item.id)">{{item.isActivated}}</v-btn></td>
            <td> 
              <GroupModal
                types="Edit"
                :isEdit="isEdit"
                :group="item"
                :getGroup="getGroup"
              />
            </td>
            <td>
              <v-menu v-model="dialogNote[item.id] "
                location="end" 
              >
                <template v-slot:activator="{ props }">
              <v-btn 
                 outlined plain size="x-small" icon v-bind="props">
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
                    <v-btn color="primary" variant="text" @click="deleteGroup(item.id)">
                      Delete
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-menu>
            </td>
          </tr>
        </tbody>
      </v-table>
    </v-spacer>
  </v-spacer>
</template>

<script>
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue";
import api from "../api";

import GroupModal from "./GroupModal.vue";
export default {
  name: "GroupComponent",
  components: {
    AppSidebar,
    AppHeader,
    GroupModal,
  },
  data() {
    return {
      isEdit: true,
      groupList: [],
      dialogNote: {},
    };
  },
  mounted() {
    this.getGroup();
    console.log(this.groupList)
  },
  methods: {
    async getGroup() {
    
       await api.get("group_list")
       .then((response) => {
        this.groupList=response
      });
    },

     async deleteGroup(id) {
       await api.delete("group_delete",{
        data:{
          id:id,
        }
       }).then((response) => {
        this.getGroup();
        return response.data;
      });
    },

    // Group Activation 
     async update_activation(id) {
      
      let data = {
        id:id,
      };
      api.put('group_activate', data).then((response) => {
        this.getGroup();
        return response.data;
      });
    },
    },
  };

</script>
<style></style>

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
            <td>{{ item.isActivated}}</td>
            <td>
              <GroupModal
                types="Edit"
                :isEdit="isEdit"
                :group="item"
                :getGroup="getGroup"
              />
            </td>
            <td>
              <v-btn
                outlined
                plain
                size="x-small"
                icon
                v-on:click="deleteGroup(item.id)"
              >
                <v-icon color="error">mdi-delete</v-icon>
              </v-btn>
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
      
      
    },
  };

</script>
<style></style>

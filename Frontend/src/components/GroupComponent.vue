<template>
    <AppSidebar />
    <AppHeader />
    <v-spacer class="page">
      <v-spacer class="d-flex page box p-3">Group</v-spacer>
      <v-spacer class="page content shadow p-3">
        
        <GroupModal types="Create"/>
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
            <td>{{ item.gname }}</td>
            <td>{{ item.start_date }}</td>
            <td>{{ item.end_date  }}</td>
            <td>{{ isActive }}</td>
            <td>
              <GroupModal types="Edit" :isEdit="isEdit"/>
            </td>
            <td>
              <v-btn outlined plain size="x-small" icon>
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
  import axios from "axios";
    import GroupModal from "./GroupModal.vue";
  export default {
    name: "DashboardComponent",
    components: {
      AppSidebar,
        AppHeader,
        GroupModal,
    },
    data() {
        return {
            isEdit: true,
            groupList: [],
            isActive: false,
      };
    },
    mounted() {
    this.getGroup();
  },
    methods: {
        async getGroup() {
            let getGroupURL = await axios.get(
                "http://127.0.0.1:8000/group_list/"
            );
            this.groupList = getGroupURL.data;
        },
    }
  };
  </script>
  <style>

  </style>
  
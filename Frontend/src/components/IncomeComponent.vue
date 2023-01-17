<template>
  <AppSidebar/>
  <AppHeader/> 
  <div class="page">
    <div class="d-flex page box p-3">Income Details</div>
    <div class="page content shadow p-3 position-relative">
      <IncomeModal type="Create" :isEdit="!isEdit" :getincome="getincome"/>
      <v-table>
        <thead>
          <tr>
            <th class="text-left">S No. #</th>
            <th class="text-left">Category</th>
            <th class="text-left">Name</th>
            <th class="text-left">Detail</th>
            <th class="text-left">Amount</th>
            <th class="text-left">Date</th>
            <th class="text-left" width="20px">Edit</th>
            <th class="text-left" width="20px">Delete</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in income" :key="item.name">
            <td>{{ i + 1 }}.</td>
            <td>{{ item.category_name }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.description }}</td>
            <td>Rs {{ item.amount  }}/-</td>
            <td>{{ item.date }}</td>
            <td>
              <IncomeModal type="Edit" :isEdit="isEdit" :income="item" :getincome="getincome"/>
            </td>
            <td>
              <v-menu v-model="dialogNote[item.id] "
                location="end" 
              >
                <template v-slot:activator="{ props }">
              <v-btn 
                 outlined plain size="28" icon v-bind="props">
                <v-icon size="15" color="error">mdi-delete</v-icon>
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
                    <v-btn color="primary" variant="text" @click="delincome(item.id)">
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
import IncomeModal from "./IncomeModal.vue";
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue";
import api from '@/api'
export default {
  mounted(){
    this.getincome()
  },

name: "IncomeComponent",
components: {
AppSidebar,
  AppHeader,
  IncomeModal,
},
data() {
return {
  isEdit:true,
  income: [],
  dialogNote: {},
}
},
methods:{
  async getincome(){
    api.get("income_list/").then((response)=>{
       this.income = response
    });
  },
  async delincome(id){
    api.delete("income_delete",{
      data:{
        id:id,
      }
    }).then ((response)=>{
      this.getincome()
      this.reset()
         return response.data
    })
  }
},

};
</script>

<style>
</style>
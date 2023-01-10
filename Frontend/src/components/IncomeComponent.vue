<template>
  <AppSidebar/>
  <AppHeader/> 
  <div class="page">
    <div class="d-flex page box p-3">Income Details</div>
    <div class="page content shadow p-3 position-relative">
      <IncomeModal type="Create" :isEdit="!isEdit" :getincomeDetails="getincomeDetails"/>
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
              <IncomeModal type="Edit" :isEdit="isEdit" :income="item" :getincomeDetails="getincomeDetails"/>
            </td>
            <td>
              <v-btn v-on:click="deldetails(item.id)" outlined plain size="x-small" icon>
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
import axios from 'axios';
import IncomeModal from "./IncomeModal.vue";
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue"
export default {
  mounted(){
    this.getincomeDetails()
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
}
},
methods:{
  async getincomeDetails(){
  let result = await axios.get("http://127.0.0.1:8000/income_list");
    this.income = result.data
   
  },
  async deldetails(id){
     await axios.delete("http://127.0.0.1:8000/income_delete",{
      data:{
      id:id
      }
     });
     this.getincomeDetails()
  }
  
    

},

};
</script>

<style>

</style>
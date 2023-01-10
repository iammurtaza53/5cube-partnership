<template>
  <AppSidebar />
  <AppHeader />
  <div class="page">
    <div class="d-flex page box p-3">Expense Details</div>
    <div class="page content shadow p-3 position-relative">
      <ExpModel type="Create" :isEdit="!isEdit" :getexpenseDetails="getexpenseDetails"/>
      <v-table style="width:100%">
        <thead>
          <tr>
            <th class="text-left" width="5%">#</th>
            <th class="text-left" width="15%">Category</th>
            <th class="text-left" width="18%">Name</th>
            <th class="text-left" width="30%">Detail</th>
            <th class="text-left" width="10%">Amount</th>
            <th class="text-left" width="12%">Date</th>
            <th class="text-left" width="5%">Edit</th>
            <th class="text-left" width="5%">Delete</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in expense" :key="item.name">
            <td>{{ i + 1 }}.</td>
            <td>{{ item.category_name }}.</td>
            <td>{{ item.name }}</td>
            <td>{{ item.description }}</td>
            <td>Rs {{ item.amount }}/-</td>
            <td>{{ item.date}}</td>
            <td>
              <ExpModel type="Edit" :isEdit="isEdit" :expense="item" :getexpenseDetails="getexpenseDetails"/>
            </td>
            <td>
              <v-btn 
                 v-on:click="deldetails(item.id)" outlined plain size="x-small" icon>
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
import ExpModel from "./ExpModel.vue";
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue";
import axios from 'axios';

export default {
  mounted(){
    this.getexpenseDetails()
  },
  
  name: "ExpenseComponent",
  components: {
    AppSidebar,
    AppHeader,
    ExpModel,
  },
 
  data() {
    return {
      isEdit:true,
      expense: [],
    };
  },
  methods:{
    async getexpenseDetails(){
      let result= await axios.get("http://127.0.0.1:8000/expense_list/");
      this.expense = result.data
      console.log(this.expense)
    },
    async deldetails(id){
       await axios.delete("http://127.0.0.1:8000/expense_delete",{
        data:{
          id:id,
        },
      });
      this.getexpenseDetails()

    }


  },
  
};
</script>

<style></style>

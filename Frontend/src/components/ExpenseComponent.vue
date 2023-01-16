<template>
  <AppSidebar />
  <AppHeader />
  <div class="page">
    <div class="d-flex page box p-3">Expense Details</div>
    <div class="page content shadow p-3 position-relative">
      <ExpModel type="Create" :isEdit="!isEdit" :getexpenses="getexpenses"/>
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
              <ExpModel type="Edit" :isEdit="isEdit" :expense="item" :getexpenses="getexpenses"/>
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
                    <v-btn color="primary" variant="text" @click="delexpenses(item.id)">
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
import ExpModel from "./ExpModel.vue";
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue";
import api from '@/api'


export default {
  mounted(){
    this.getexpenses()
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
      dialogNote: {},
    };
  },
  methods:{
    async getexpenses(){
       api.get('expense_list/').then((response)=>{
         this.expense = response
      });
    },
    async delexpenses(id){
      api.delete("expense_delete",{
        data:{
          id:id,
        }
      }).then((response)=>{
        this.getexpenses()
        return response.data
      });
    },


  },
  
};
</script>

<style></style>

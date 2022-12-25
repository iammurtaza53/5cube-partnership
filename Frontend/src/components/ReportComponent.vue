<template>
  <AppSidebar />
  <AppHeader />

  <v-spacer class="page">
    <v-spacer class="d-flex page box p-3">Report</v-spacer>
    <v-spacer class="page content shadow p-3">
    
  <v-table class="border-bottom" >
    <thead class="bg">
      <tr class="font-weight-bold" >
         <th class="text-left">#</th>
        <th class="text-left">Expense by Category</th>
        <th class="text-left">Amount</th>
      </tr>
    </thead>
    <tbody>
        <tr v-for="(item, i) in report " :key="item.amount">
            <td>{{i+1}}</td>
            <td>{{item.expense}}</td>
            <td>Rs {{item.amount}}/-</td>
             
     </tr>
      <tr class="font-weight-bold">
      <td></td>
      <td>Total</td>
      <td>Rs {{sum}}/-</td>
      </tr>         
    </tbody> 
  </v-table>
  <v-table class="border-bottom">
    <thead class="bg">
     <tr class="font-weight-bold">
         <th class="text-left">#</th>
        <th class="text-left">Income by Category</th>
        <th class="text-left">Amount</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(itm,i) in data" :key="itm.Amount">
        <td>{{i+1}}.</td>
        <td>{{itm.income}}</td>
        <td>Rs {{itm.Amount}}/-</td>
      </tr>
   
      <tr class="font-weight-bold">
      <td></td>
      <td>Total</td>
      <td>Rs{{total}}/-</td>
      </tr>         
    </tbody>
  </v-table>
  <v-row>
  <v-col sm="6">
  <v-table>
     <thead class="bg">
     <tr class="font-weight-bold">
         <th class="text-left">#</th>
        <th class="text-left">Person</th>
        <th class="text-left">Salary</th>
         <th class="text-left">Share</th>
          <th class="text-left">Income</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(itm,i) in items" :key="itm.salary">
        <td>{{i+1}}</td>
        <td>{{itm.person}}</td>
        <td>Rs {{itm.salary}}/-</td>
        <td>{{itm.share}}%</td>
        <td>Rs {{itm.income}}/-</td>

      </tr>

    
    </tbody>
    
  </v-table>
  </v-col>
  <v-col sm="6">
    <v-table>
      
      <tbody>
        <!-- <tr v-for="(item) in itm" :key="item.company">
       
        <th>{{item.company}}</th>
        <td>Rs {{item.income}}/-</td>
        
        
      </tr> -->
      <tr>
      <th>Company Income</th>
      <td>Rs {{total}}/-</td>
      </tr>
      <tr>
      <th>Company Expense</th>
      <td>Rs {{sum}}/-</td>
      </tr>
      <tr>
        <th>Company Profit</th>
        <td>Rs {{alltotal}}/-</td>
      </tr>

    




 
      </tbody>
    </v-table>
  </v-col>
  </v-row>

 

   
    </v-spacer>
  </v-spacer>
</template>

<script>
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue";

export default {
  name: "ReportComponent",
  components: {
    AppSidebar,
    AppHeader,
  },
  data() {
    return {
     
    report:[
        {
         expense: "Office Rent",
         amount: 15999,

        },
        {
         expense: "Laptop Repair",
         amount: 9680,
        },
        {
         expense: "Bill",
         amount: 10080,
        },

    ],
    data:[
      {
       income:"clients",
       Amount:98991,
      }
    ],
    items:[
      {
       person:"Alex",
       salary:10000,
       share:40,
       income:27292.8,

      },
      {
         person:"Tanzeema",
       salary:10000,
       share: 60,
       income: 35939.2,
      },
    ],
    };
  },
  methods(){},
  computed:{
    sum()
    {
      return this.report.reduce((sum ,item) => item.amount  + sum,0)
    },
   total(){
    return this.data.reduce((total,itm)=> itm.Amount + total,0)
   },
   alltotal(){
    return (this.total - this.sum)
   }
  },
    
};
</script>
<style>
.border-bottom{
  
  border-bottom: 1px solid rgb(216, 216, 216);

}
.bg{
  background-color: rgb(250, 208, 191);
}

</style>




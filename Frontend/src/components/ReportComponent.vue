<template>
  <AppSidebar />
  <AppHeader />

  <v-spacer class="page">
    <v-spacer class="d-flex page box p-3">Report</v-spacer>
    <v-spacer class="page content shadow p-3">
    
  <v-table >
    <thead>
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
            <td>Rs{{item.amount}}/-</td>
             
     </tr>
      <tr class="font-weight-bold">
      <td></td>
      <td>Total</td>
      <td>Rs87650000/-</td>
      </tr>         
    </tbody> 
  </v-table>
  <v-table class="border">
    <thead>
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
        <td>Rs{{itm.Amount}}/-</td>
      </tr>
   
      <tr class="font-weight-bold">
      <td></td>
      <td>Total</td>
      <td>Rs87650000/-</td>
      </tr>         
    </tbody>
  </v-table>
  <v-col sm="6">
   
  <v-table>
     <thead>
     <tr class="font-weight-bold">
         <th class="text-left">#</th>
        <th class="text-left">Person</th>
        <th class="text-left">Salary</th>
         <th class="text-left">Share</th>
          <th class="text-left">Income</th>
      </tr>
    </thead>
    <tbody></tbody>
  </v-table>
  </v-col>
   
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
    ]
    };
  },
};
</script>
<style>
.border{
  
  border-bottom: 1px solid;

}

</style>




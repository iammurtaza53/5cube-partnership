<template>
  <AppSidebar />
  <AppHeader />

  <v-spacer class="page">
    <v-spacer class="d-flex page box p-3">Report</v-spacer>
    <v-spacer class="page content shadow p-3">
      <v-table class="border-bottom">
        <thead class="bg">
          <tr class="font-weight-bold">
            <th class="text-left">#</th>
            <th class="text-left">Expense by Category</th>
            <th class="text-left">Amount</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, i) in expense" :key="item.eamount">
            <td>{{ i + 1 }}</td>
            <td>{{ item.ename }}</td>
            <td>Rs {{ item.eamount }}/-</td>
          </tr>
          <tr class="font-weight-bold">
            <td></td>
            <td>Total</td>
            <td>Rs {{ getexpenses() }}/-</td>
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
          <tr v-for="(itm, i) in income" :key="itm.iamount">
            <td>{{ i + 1 }}.</td>
            <td>{{ itm.iname }}</td>
            <td>Rs {{ itm.iamount }}/-</td>
          </tr>

          <tr class="font-weight-bold">
            <td></td>
            <td>Total</td>
            <td>Rs{{ getincome() }}/-</td>
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
              <tr v-for="(itm, i) in items" :key="itm.salary">
                <td>{{ i + 1 }}</td>
                <td>{{ itm.person }}</td>
                <td>Rs {{ itm.salary }}/-</td>
                <td>{{ itm.share }}%</td>
                <td >Rs {{ itm.shares }}/-</td>
              </tr>
            </tbody>
          </v-table>
        </v-col>
        <v-col sm="6">
          <v-table>
            <tbody>
              <tr>
                <th>Total Income</th>
                <td>Rs {{getincome()}}/-</td>
              </tr>
              <tr>
                <th>Total Expense</th>
                <td>Rs {{ getexpenses() }}/-</td>
              </tr>
              <tr>
                <th>Net Profit</th>
                <td>Rs {{ alltotal }}/-</td>
              </tr>
            </tbody>
          </v-table>
        </v-col>
      </v-row>
    </v-spacer>
  </v-spacer>
</template>

<script>
import axios from "axios";
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue";

export default {
  mounted() {
    this.getedata();
    this.getidata();
    this.calculateShares();
   
 

  },
  name: "ReportComponent",
  components: {
    AppSidebar,
    AppHeader,
  },
  data() {
    return {
    
      expense: [],
      income: [],
      items: [
        {
          person: "Tom",
          salary: 50000,
          share: 30,
          shares:0
        },
        {
          person: "John",
          salary: 50000,
          share: 70,
          shares:0
        },
      ],
      
    };
  },
  methods: {
    async getedata() {
      let result = await axios.get("http://127.0.0.1:8000/expense_list/");
      this.expense = result.data;
    },
    async getidata() {
      let result = await axios.get("http://127.0.0.1:8000/income_list/");
      this.income = result.data;

    },
     getincome() {
      this.income.iamount=this.income.map((e)=>e.iamount)
           return this.income.reduce((total, itm) => itm.iamount + total, 0);

      
    },
    getexpenses() {
      this.expense.eamount=this.expense.map((e)=>e.eamount)
      return this.expense.reduce((total,itm)=>itm.eamount +total,0);
    },
    calculateShares() {
      setTimeout(()=>{
      this.items.shares=this.items.map((e) => {
        return ((this.alltotal * e.share ) / 100)+e.salary;
        
      });
     
    
      this.items[0].shares=this.items.shares[0]
      this.items[1].shares=this.items.shares[1]
      },1000)
  
    },
  
  },

  computed: {
    alltotal() {
      return this.getincome() - this.totalsalary - this.getexpenses();
    },
    totalsalary() {
      return this.items.reduce((total, itm) => itm.salary + total, 0);
         
    },
   
  },
};
</script>
<style>
.border-bottom {
  border-bottom: 1px solid rgb(216, 216, 216);
}
.bg {
  background-color: rgb(250, 208, 191);
}
</style>




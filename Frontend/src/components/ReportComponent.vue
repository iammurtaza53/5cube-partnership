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
          <tr v-for="(item, i) in expense" :key="item.amount">
            <td>{{ i + 1 }}</td>
            <td>{{ item.name }}</td>
            <td>Rs {{ item.amount }}/-</td>
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
          <tr v-for="(itm, i) in income" :key="itm.amount">
            <td>{{ i + 1 }}.</td>
            <td>{{ itm.name }}</td>
            <td>Rs {{ itm.amount }}/-</td>
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
  <div>
  <apexchart width="500" type="bar" :options="options" :series="series"></apexchart>
</div>
</template>

<script>
import axios from "axios";
import AppSidebar from "./AppSidebar.vue";
import AppHeader from "./AppHeader.vue";


import api from "../api";
export default {
  mounted() {
    this.getedata();
    this.getidata();
    this.calculateShares();
    this.activegroup_filter();
  },
  name: "ReportComponent",
  components: {
    AppSidebar,
    AppHeader,
  },
  data() {
    return {
      options: {
        chart: {
          id: 'vuechart-example'
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998]
        }
      },
      series: [{
        name: 'series-1',
        data: [30, 40, 45, 50, 49, 60, 70, 91]
      }],
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
    async activegroup_filter() {
      await api.get("activegroup_filter").then((response) => {
        console.log("response",response);
      });
    },
    async getedata() {
      let result = await axios.get("http://127.0.0.1:8000/expense_list/");
      this.expense = result.data;
    },
    async getidata() {
      let result = await axios.get("http://127.0.0.1:8000/income_list/");
      this.income = result.data;
    },
    
     getincome() {
      this.income.amount=this.income.map((e)=>e.amount)
           return this.income.reduce((total, itm) => itm.amount + total, 0);
    },
    getexpenses() {
      this.expense.amount=this.expense.map((e)=>e.amount)
      return this.expense.reduce((total,itm)=>itm.amount +total,0);
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
<style scope>
.border-bottom {
  border-bottom: 1px solid rgb(216, 216, 216);
}
.bg {
  background-color: rgb(250, 208, 191);
  border-radius: none;
}

</style>




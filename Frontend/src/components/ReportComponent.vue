<template>
  <AppSidebar />
  <AppHeader />

  <v-spacer class="page">
    <v-spacer class="d-flex page box p-3">Report</v-spacer>
    <v-spacer class="page content shadow p-3">

    <!-- <div class="exp mt-6 pa-3 text-center" >Expenses</div> -->
    <v-container>
    <v-row>
     
    <v-container>
      <v-row >
        <v-col sm="6" class="height">
          <v-sheet class="expsheet pt-4 " elevation="4" >
           
            <v-table class="height" >
              <thead>
                <tr class="font-weight-bold">
                  <th class="text-left">Expenses</th>
                  <th class="text-left">Expense by Category</th>
                  <th class="text-left">Amount</th>
                </tr>
              </thead>
              <tbody>
                <tr  class="bg " v-for="(item, i) in expense" :key="item.amount">
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
          </v-sheet>
        </v-col>
        
        <v-col  sm="6" class="height">
          <v-sheet class="expsheet pt-4" elevation="4">
             
            <v-table class="height">
              <thead>
                <tr class="font-weight-bold">
                  <th class="text-left">#</th>
                  <th class="text-left">Income by Category</th>
                  <th class="text-left">Amount</th>
                </tr>
              </thead>
              <tbody>
                <tr class="bg" v-for="(itm, i) in income" :key="itm.amount">
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
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
    <v-col sm="6" >
         <v-sheet class=" card pt-4" elevation="4">
            <div>
    <apexchart :options="chartOptions" :series="chartData" type="pie"></apexchart>
  </div>
         </v-sheet>
        </v-col>
      <v-col sm="6" class="height">
         <v-sheet class="sheet pt-4 " elevation="4">
        <v-table>
          <tbody>
            <tr class="bg">
              <th>Total Income</th>
              <td >Rs {{ getincome() }}/-</td>
            </tr>
            <tr class="bg">
              <th>Total Expense</th>
              <td>Rs {{ getexpenses() }}/-</td>
            </tr>
            <tr class="bg">
              <th>Net Profit</th>
              <td>Rs {{ alltotal }}/-</td>
            </tr>
          </tbody>
        </v-table>
         </v-sheet>
      </v-col>
       
    </v-row>
    </v-container>
    <!-- <v-row>
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
          <tbody>
            <tr v-for="(itm, i) in items" :key="itm.salary">
              <td>{{ i + 1 }}</td>
              <td>{{ itm.person }}</td>
              <td>Rs {{ itm.salary }}/-</td>
              <td>{{ itm.share }}%</td>
              <td>Rs {{ itm.shares }}/-</td>
            </tr>
          </tbody>
        </v-table>
      </v-col>
      <v-col sm="6">
        <v-table>
          <tbody>
            <tr>
              <th>Total Income</th>
              <td>Rs {{ getincome() }}/-</td>
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
    </v-row> -->
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
          shares: 0,
        },
        {
          person: "John",
          salary: 50000,
          share: 70,
          shares: 0,
        },
      ],
    chartOptions: {
      chart: {
        width: 280,
   
        type: 'pie',
            },
      labels: ['John', 'Tom'],
      colors:['#510f13', '#dc8c8c'],
        },
    chartData: [],
      
    
    



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
      this.income.amount = this.income.map((e) => e.amount);
      return this.income.reduce((total, itm) => itm.amount + total, 0);
    },
    getexpenses() {
      this.expense.amount = this.expense.map((e) => e.amount);
      return this.expense.reduce((total, itm) => itm.amount + total, 0);
    },
    calculateShares() {
      setTimeout(() => {
        this.items.shares = this.items.map((e) => {
           
          return (this.alltotal * e.share) / 100 + e.salary;
          
        });
       
       
        this.items[0].shares = this.items.shares[0];
        this.items[1].shares = this.items.shares[1];
       this.chartData=this.items.shares
        console.log( this.chartData)
      }, 1000);
        
    },
//     getsalary(){
//       this.items.shares= this.items.map((e)=>e.shares)
          
//         this.chartData= this.items.shares
      
//
//     }
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
/* .border {
  border-collapse: collapse;
  width: 100%;
} */
.expsheet {
  width: 100%;
  height: 50vh ;
  overflow: auto;
 
  border: 1px solid rgb(201, 197, 197);
}
.sheet{
    width: 100%;
  height: 62vh ;
  overflow: auto;
 
  border: 1px solid rgb(201, 197, 197);
}
.text-color{
  color: #501519f1;

}
.font-weight-bold{
 
  font-size: 30px;
  color:grey;
}
th{
   font-size: 12px !important;
}
td{
  height: 30px !important;
 font-size: 12px !important;
}
.card{
  border: 1px solid rgb(224, 224, 224);
  width: 100%;
}


/* .border-bottom {
  border-bottom: 1px solid rgb(216, 216, 216);
} */
/* .exp {
  border-collapse: collapse;
  background-color: #501519f1;
  color: whitesmoke;

  font-size: 25px;
} */
.bg:nth-child(odd){
  background-color: rgb(238, 235, 235);
  
}

/* background-color: rgb(250, 208, 191); */
</style>




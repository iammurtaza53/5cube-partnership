<template>
  <v-dialog v-model="dialog" persistent max-width="500">
    <template v-slot:activator="{ props }">
      <div v-if="!isEdit">
        <v-btn color="success" class="ma-4" v-bind="props">{{ type }}</v-btn>
      </div>
      <div v-if="isEdit">
        <v-btn 
        outlined plain size="x-small" icon v-bind="props" @click="prefill(isprefill)">
          <v-icon color="indigo">mdi-pencil</v-icon>
        </v-btn>
      </div>
    </template>

    <v-card>
      <v-card-title> 
        <span class="text-h5">{{ type }} Income</span>
      </v-card-title>
      <v-divider color="white" class="divider"></v-divider>
      <v-card-text>
        <v-container>
          <v-row>
            <v-select v-model="iname" :items="Incategories" label="Name*" required>
            </v-select>
           
          </v-row>
          <v-row>
            <v-textarea v-model="idetail" label="Detail*" rows="1"></v-textarea>
          </v-row>
          <v-row>
            <v-text-field
              v-model="iamount"
              label="Amount*"
              placeholder="Enter Amount"
              required
            ></v-text-field>
          </v-row>
        </v-container>
        <small>*indicates required field</small>
      </v-card-text>
      <v-divider color="white" class="divider"></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="white" :style="{ backgroundColor: '#e91e62' }" elevation="4"
          @click="dialog = false">Close</v-btn>
        <v-btn color="white" :style="{ backgroundColor: 'blue' }" elevation="4" 
           :disabled="disablebtn"
            @click="isEdit ? updateincome(isprefill.id):postIncome(); 
            dialog=false;">save</v-btn>
      </v-card-actions>
    </v-card> 
  </v-dialog>
</template>
<script>

import axios from 'axios'
export default {
    mounted(){
        this.getincome()
    },

    props:{
        type:String,
        isEdit:Boolean,
      isprefill: Object,
      getincomeDetails: Function,
    },
    data(){
        return{
     dialog: false,
      iname: "",
      idetail: "",
      iamount: "",
      Incategories: [],
    };  
    },
    methods:{
      async updateincome(id){
         await axios.put("http://127.0.0.1:8000/income_update",{
          id:id,
          iname:this.iname,
          idetail:this.idetail,
          iamount:this.iamount,
         });
         this.getincomeDetails()
          // console.log("udateincome",this.updateincome)
      },
     

      async prefill(isprefill){
        this.iname = isprefill.iname,
        this.idetail= isprefill.idetail,
        this.iamount = isprefill.iamount,
        console.log("prefill form",isprefill)
      },
        async getincome(){
      let result = await axios.get(
        "http://localhost:8000/category_type?type=Income"
      ); 
      this.Incategories = result.data;
      this.Incategories = this.Incategories.map((item)=>(item.cname)
      )
        },
         async postIncome(){
     let result = await axios.post("http://127.0.0.1:8000/income_create",{
        iname: this.iname,
        iamount:this.iamount,
        idetail:this.idetail,
     });
      
           this.postIncome = result.data;
           this.getincomeDetails()
           this.refresh()
    },
        
    refresh(){
      this.iname = "";
      this.idetail = "";
      this.iamount = "";
    },

    },
    computed:{
      disablebtn(){
       return (this.Name == "" || this.Detail == "" || this.Amount == "");
        
      }
    },
};

</script>

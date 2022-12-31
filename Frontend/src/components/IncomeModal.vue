<template>
  <v-dialog v-model="dialog" persistent max-width="500">
    <template v-slot:activator="{ props }">
      <div v-if="!isEdit">
        <v-btn color="success" class="ma-4" v-bind="props">{{ type }}</v-btn>
      </div>
      <div v-if="isEdit">
        <v-btn outlined plain size="x-small" icon v-bind="props">
          <v-icon color="indigo">mdi-pencil</v-icon>
        </v-btn>
      </div>
    </template>

    <v-card>
      <v-card-title> 
        <span class="text-h5">{{ type }} {{ isEdit ? "Income":"Income Detail" }}</span>
      </v-card-title>
      <v-divider color="white" class="divider"></v-divider>
      <v-card-text>
        <v-container>
          <v-row>
            <v-select v-model="Name" :items="Incategories" label="Name*" required>
            </v-select>
           
          </v-row>
          <v-row>
            <v-textarea v-model="Detail" label="Detail*" rows="1"></v-textarea>
          </v-row>
          <v-row>
            <v-text-field
              v-model="Amount"
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
           :disabled="disablebtn" @click="postCategories(); dialog=false;">save</v-btn>
      </v-card-actions>
    </v-card> -->


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
    },
    data(){
        return{
     dialog: false,
      Name: "",
      Detail: "",
      Amount: "",
      Incategories: [],
    };  
    },
    methods:{
        async getincome(){
      let result = await axios.get(
        "http://localhost:8000/category_type?type=Income"
      ); 
      this.Incategories = result.data;
      this.Incategories = this.Incategories.map((item)=>(item.cname)
      )
        console.log(this.Incategories) 
        },
         async postInCategories(){
     let result = await axios.post("http://127.0.0.1:8000/expense_create",{
        ename: this.Name,
        eamount:this.Amount,
        edetail:this.Detail,
      });
      this.postCategories= result.data;
      console.log (this.postCategories)

       
    },
        


    },
    computed:{
      disablebtn(){
       return (this.Name == "" || this.Detail == "" || this.Amount == "");
        
      }
    },
};

</script>

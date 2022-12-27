 <template>
  <!---category component model start---->
    <v-row justify="start">
     <v-dialog v-model="dialog"  persistent max-width="500">
       <template v-slot:activator="{ props }">
         <div v-if="types=='Create'">
           <v-btn  color="success" class="ma-4" v-bind="props">{{ types }}</v-btn>
         </div>
        <div v-if="types=='Edit'">
           <v-btn v-on:click="updateData(item.id)" outlined plain size="x-small" icon v-bind="props">
             <v-icon color="indigo">mdi-pencil</v-icon>
          </v-btn>
         </div>
      </template>

       <v-card>
        <v-card-title>
           <span class="text-h5">{{ types }} Category</span>
         </v-card-title>
         <v-divider color="white" class="divider"></v-divider>
         <v-card-text>
           <v-container>
            <v-row>
               <v-col>
                 <v-text-field
                  v-model="name"
                   label="Category Name*"
                   placeholder="Enter Category Name"
                   required
                 ></v-text-field>
             </v-col>
            </v-row>
             <v-row no-gutters>
               <v-col>
                 <v-select
                 v-model="type"
                 :items="['Expense', 'Income']"
                 label="Category type*"
                   required
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
         </v-card-text>
       <v-divider color="white" class="divider"></v-divider>
        <v-card-actions>
         <v-spacer></v-spacer>
          <v-btn
            color="white"
             :style="{ backgroundColor: '#e91e62' }"
             elevation="4"
             @click="dialog = false"
           >
             Close
           </v-btn>
           <v-btn
             color="white"
             :style="{ backgroundColor: 'blue' }"
            elevation="4"
            :disabled="disablebtn"
             @click="sendData"
           >
             Save
           </v-btn>
         </v-card-actions>
      </v-card>
     </v-dialog>
  </v-row>
</template>
<script>
import axios from "axios";
export default {
  props: {
    types: String,
  },
  data() {
    return {
      dialog: false,
      name:"",
      type:"",
    };
  },
   
  methods: {
    
       


    async sendData(){

      console.log(this.name,this.type);
      let result= await axios.post("http://localhost:3000/category",{
        name:this.name,
        type:this.type,
      });
      console.warn("result",result);
    },
 
    
  
  computed: {
      disablebtn() {
       return(this.name=="" || this.category =="")

      },
     
     },
}
      
} 

</script>
<style scope>
.aaa {
  border: 3px solid red;
}
</style>

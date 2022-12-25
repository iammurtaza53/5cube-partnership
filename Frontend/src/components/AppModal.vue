 <template>
  <!---category component model start---->
    <v-row justify="start">
     <v-dialog v-model="dialog" persistent max-width="500">
       <template v-slot:activator="{ props }">
         <div v-if="type=='Create'">
           <v-btn  color="success" class="ma-4" v-bind="props">{{ type }}</v-btn>
         </div>
        <div v-if="type=='Edit'">
           <v-btn outlined plain size="x-small" icon v-bind="props">
             <v-icon color="indigo">mdi-pencil</v-icon>
          </v-btn>
         </div>
      </template>

       <v-card>
        <v-card-title>
          <span class="text-h5">{{ type }} Category</span>
        </v-card-title>
        <v-divider color="white" class="divider"></v-divider>
        <v-card-text>
          <v-container>
            <v-row>
               <v-col>
                 <v-text-field
                   label="Category Name*"
                   placeholder="Enter Category Name"
                   required
                 ></v-text-field>
             </v-col>
            </v-row>
             <v-row no-gutters>
               <v-col>
                 <v-select
                 :items="['Expense', 'Income']"
                 label="Category type*"
                   required
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
        <!-- </form> -->
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
             @click="dialog = false"
           >
             Save
           </v-btn>
         </v-card-actions>
      </v-card>
     </v-dialog>
  </v-row>
</template>
<script>
export default {
  props: {
    type: String,
  },
  data() {
    return {
      categories: [],
      catForm: {
        name: "",
        type: "",
      },
      dialog: false,
    };
  },
  methods: {},
  // computed: {
  //     myfunc() {
  //         return console.log("myname3")
  //     }
  // }
};
</script>
<style scope>
.aaa {
  border: 3px solid red;
}
</style>

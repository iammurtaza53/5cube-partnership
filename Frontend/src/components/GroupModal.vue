<template>
  <!---category component model start---->
  <v-row justify="start">
    <v-dialog v-model="dialog" persistent max-width="500">
      <template v-slot:activator="{ props }">
        <div v-if="types == 'Create'">
          <v-btn color="success" class="ma-4" v-bind="props">{{ types }}</v-btn>
          <!--  -->
        </div>
        <div v-if="types == 'Edit'">
          <v-btn outlined plain size="x-small" icon v-bind="props">
            <v-icon color="indigo">mdi-pencil</v-icon>
          </v-btn>
        </div>
      </template>

      <div v-if="types == 'Create'">
        <v-card>
          <v-card-title>
            <span class="text-h5">Create Category</span>
          </v-card-title>
          <v-divider color="white" class="divider"></v-divider>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <datepicker
                    v-model="start_date"
                    class="date-picker"
                    placeholder="Select Starting Date"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <datepicker
                    v-model="end_date"
                    class="date-picker"
                    placeholder="Select Ending Date"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-text-field
                    label="Name*"
                    placeholder="Enter Group Name"
                    required
                    v-model="gname"
                  ></v-text-field>
                </v-col>
              </v-row>

              <br />
              <br />
           
             
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
              :disabled="disablebtn"
              @click="
                createGroup();
                dialog = false;
              "
            >
              <!-- @click="$emit('create-categories')" -->
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </div>

      <div v-if="types == 'Edit'">
        <v-card>
          <v-card-title>
            <span class="text-h5">Edit Category</span>
          </v-card-title>
          <v-divider color="white" class="divider"></v-divider>
          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <v-text-field
                    :value="category.cname"
                    placeholder="Enter Category Name"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row no-gutters>
                <v-col>
                  <v-select
                    :value="category.ctype"
                    :items="['Expense', 'Income']"
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
              :disabled="disablebtn"
              @click="
                createCategories();
                dialog = false;
              "
            >
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </div>
    </v-dialog>
  </v-row>
</template>
<script>
import axios from "axios";
// import Datepicker from "  ";
import Datepicker from "vue3-datepicker";
export default {
  components: {
    Datepicker,
    // datepicker,
  },
  props: {
    types: String,
    getCategories: Function,
    category: Object,
  },

  mounted() {
    // if (this.types == "Ed") {
    // this.getCategoryById(this.categoryId);
    // }
  },
  data() {
    return {
      dialog: false,
      gname: "",
      start_date: Date,
      end_date: Date,
    };
  },
  methods: {
    // async getCategoryById(id) {
    //   await axios.get("http://127.0.0.1:8000/catinfo/" + id)
    // }

    async updateCategories() {
      await axios.put("http://127.0.0.1:8000/category_update", {
        cname: this.cname,
        ctype: this.ctype,
      });
    },
    async createGroup() {
      await axios.post("http://127.0.0.1:8000/group_create", {
        gname:this.gname,
        start_date: this.start_date,
        end_date: this.end_date,
      });
      // this.reset();
    },
    // reset() {
    //   this.gname = "";
    // },
  },
  computed: {
    disablebtn() {
      return this.gname == "" || this.start_date.value == "" || this.end_date.value == "";
    },
  },
};
</script>
<style scope>
.aaa {
  border: 3px solid red;
}
.date-picker {
    font-size: 16px;
  padding: 20px;
  width: 100%;
  border: 1px solid #8e8e8e;
  background-color: #f0f0f0;
  border-top: none;
  border-left: none;
  border-right: none;
}
.date-picker:hover {
  background-color: #e8e8e8;
  border-bottom: 1px solid black;
}
.date-picker:focus {
  border-bottom: 2px solid black;
  outline: none;
  background-color: #e1e1e1;
}
</style>

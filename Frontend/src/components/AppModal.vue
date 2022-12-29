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
                  <v-text-field
                    label="Category Name*"
                    placeholder="Enter Category Name"
                    required
                    v-model="cname"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row no-gutters>
                <v-col>
                  <v-select
                  v-model="ctype"
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
              :disabled="disablebtn"
              @click="
                createCategories();
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
                    label="Category Name*"
                    placeholder="Enter Category Name"
                    required
                    v-model="cname"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row no-gutters>
                <v-col>
                  <v-select
                    v-model="ctype"
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
export default {
  props: {
    types: String,
    getCategories: Function,
  },
  data() {
    return {
      dialog: false,
      cname: "",
      ctype: "",
    };
  },

  methods: {
    
     
  
    async updateCategories() {
      await axios.put("http://127.0.0.1:8000/category_update", {
        cname: this.cname,
        ctype: this.ctype,
      });
    },
    async createCategories() {
      await axios.post("http://127.0.0.1:8000/category_create", {
        cname: this.cname,
        ctype: this.ctype,
      });
      this.getCategories();
      this.reset();
    },
    reset() {
      this.cname = "";
      this.ctype = "";
    },
  },
  computed: {
    disablebtn() {
      return this.cname == "" || this.ctype == "";
    },
  },
};
</script>
<style scope>
.aaa {
  border: 3px solid red;
}
</style>

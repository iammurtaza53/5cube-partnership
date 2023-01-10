<template>
  <!---category component model start---->

  <v-dialog v-model="dialog" persistent max-width="500">
    <template v-slot:activator="{ props }">
      <div v-if="!isEdit">
        <v-btn color="success" class="ma-4" v-bind="props">{{ types }}</v-btn>
      </div>
      <div v-if="isEdit">
        <v-btn
          outlined
          plain
          size="x-small"
          icon
          v-bind="props"
          @click="prefillForm(category)"
        >
          <v-icon color="indigo">mdi-pencil</v-icon>
        </v-btn>
      </div>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">{{ types }} Category </span>
        <!-- {{!isEdit ? "Edit":"Category"}} -->
      </v-card-title>
      <v-divider color="white" class="divider"></v-divider>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col>
              <v-text-field
                label=" Name*"
                placeholder="Enter Name"
                required
                v-model="name"
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
          >Close</v-btn
        >
        <v-btn
          color="white"
          :style="{ backgroundColor: 'blue' }"
          elevation="4"
          :disabled="disablebtn"
          @click="
            isEdit ? updateCategories(category.id) : createCategories();
            dialog = false;
          "
          >Save</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from "axios";
export default {
  props: {
    types: String,
    getCategories: Function,
    isEdit: Boolean,
    category: Object,
  },
  mounted() {},
  data() {
    return {
      dialog: false,
      name: "",
      type: "",
    };
  },

  methods: {
    async updateCategories(id) {
      await axios.put("http://127.0.0.1:8000/category_update", {
        id: id,
        name: this.name,
        type: this.type,
      });
      this.getCategories();
    },
    async prefillForm(category) {
      this.name = category.name;
      this.type = category.type;
    },
    async createCategories() {
      await axios.post("http://127.0.0.1:8000/category_create", {
        name: this.name,
        type: this.type,
      });
      this.getCategories();
      this.reset();
    },
    reset() {
      this.name = "";
      this.type = "";
    },
  },
  computed: {
    disablebtn() {
      return this.name == "" || this.type == "";
    },
  },
};
</script>
<style scope>
.aaa {
  border: 3px solid red;
}
</style>

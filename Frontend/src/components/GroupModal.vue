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
          size="28"
          icon
          v-bind="props"
          @click="prefillForm(group)"
        >
          <v-icon size="15" color="indigo">mdi-pencil</v-icon>
        </v-btn>
      </div>
    </template>
    <v-card>
      <v-card-title>
        <span class="text-h5">{{ types }} Group </span>
        <!-- {{!isEdit ? "Edit":"Category"}} -->
      </v-card-title>
      <v-divider color="white" class="divider"></v-divider>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col>
              <v-text-field type="date" v-model="start_date"></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-text-field type="date" v-model="end_date"></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-text-field
                label="Name*"
                placeholder="Enter Group Name"
                required
                v-model="name"
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
          @click="
            dialog = false;
            reset();
          "
          >Close</v-btn
        >
        <v-btn
          color="white"
          :style="{ backgroundColor: 'blue' }"
          elevation="4"
          :disabled="disablebtn"
          @click="
            isEdit ? updateGroup(group.id) : createGroup();
            dialog = false;
          "
          >Save</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import api from "../api";


export default {
  name: "GroupModal",
  components: {
    
  },
  props: {
    types: String,
    getGroup: Function,
    group: Object,
    isEdit: Boolean,
  },

  data() {
    return {
      dialog: false,
      name: "",
      start_date: null ,
      end_date: null,
    };
  },
  methods: {
    prefillForm(group) {
      this.name = group.name;
      this.start_date = group.start_date;
      this.end_date = group.end_date;
    },
    async updateGroup(id) {
      let data = {
        id:id,
        name:this.name,
        start_date: this.start_date,
        end_date:  this.end_date
      };
      api.put("group_update", data).then((response) => {
        this.getGroup();
        return response.data;
      });
    },

    async createGroup() {
       let data = {
        name:this.name,
        start_date: this.start_date,
        end_date: this.end_date
      };
      api.post("group_create", data).then((response) => {
        this.getGroup();
        this.reset();
        return response.data;

      });
    },
    reset() {
      this.name = "";
      this.start_date = null;
      this.end_date = null;
    },
    },


  computed: {
    disablebtn() {
      return this.name == "" || this.start_date == "" || this.end_date== "";
    },
  },
};
</script>
<style scope>
.aaa {
  border: 3px solid red;
}

</style>

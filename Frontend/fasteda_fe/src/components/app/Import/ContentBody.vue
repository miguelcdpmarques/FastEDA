<template>
    <div class="content-body">
        <div class="content-section">
            <div class="form-group">
                <form enctype="multipart/form-data">
                    <label class="btn btn-upload">
                        Browse... <input type="file" hidden ref="file" @change="handleFileUpload">
                    </label>
                </form>
            </div>
            <small>Supported formats: <em>.csv</em></small>
        </div>
        <div class="section-preview">
            <h3>Preview</h3>
            <hr>
            <div data-spy="scroll" data-target="#navbar-example2" data-offset="0">
                <h4 id="fat">SheetName</h4>
                <table class="table">
                    <thead class="thead-light">
                        <tr>
                            <th scope="col">#</th>
                            <th scope="col">First</th>
                            <th scope="col">Last</th>
                            <th scope="col">Handle</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th scope="row">1</th>
                            <td>Mark</td>
                            <td>Otto</td>
                            <td>@mdo</td>
                        </tr>
                        <tr>
                            <th scope="row">2</th>
                            <td>Jacob</td>
                            <td>Thornton</td>
                            <td>@fat</td>
                        </tr>
                        <tr>
                            <th scope="row">3</th>
                            <td>Larry</td>
                            <td>the Bird</td>
                            <td>@twitter</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="section-next">
            <button class="btn btn-next">Next</button>
        </div>
    </div>
</template>

<script>

export default {
    name: 'ContentBody',
    data() {
        return {
            csv_table: ''
        }
    },
    computed: {
        filename() {
            return this.$store.state.filename
        }
    },
    watch: {
        previewData(oldData, newData) {
            this.csv_table = 'Loading...'
            console.log("Use watcher to call api asynchronously after post request completed")
        }
    },
    methods: {
        submitFile() {
            console.log(this.file)
            let formData = new FormData();
            formData.append('file', this.file);
            var config = {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }
            this.$store.dispatch('upload', {formData, config})
        },
        handleFileUpload() {
            this.file = this.$refs.file.files[0];
            console.log(this.file);
            this.submitFile()
        }
    }
}
</script>

<style>
</style>

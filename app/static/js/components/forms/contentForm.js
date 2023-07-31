import {html, reactive, watch} from "../../packages/arrow.js"


const postOptions = html`
    <div class="formGroup">
        <label for="title">Title</label>
        <input type="text" name="title" id="inputTitle">
    </div>
    <div class="formGroup">
            <label for="content">Content</label>
            <textarea name="content" id="inputContent" cols="30" rows="5"></textarea>
    </div>
`

const seriesOptions = html`
    <div class="formGroup">
        <label for="seriesName">Series Name</label>
        <input type="text" name="seriesName" id="inputSeriesName">
    </div>
    <div class="formGroup">
            <label for="description">Description</label>
            <textarea name="description" id="inputDescription" cols="30" rows="5"></textarea>
    </div>
`

const projectOptions = html`
    <div class="formGroup">
        <label for="projectName">Project Name</label>
        <input type="text" name="projectName" id="inputTitle">
    </div>
    <div class="formGroup">
            <label for="description">Description</label>
            <textarea name="content" id="inputDescription" cols="30" rows="5"></textarea>
    </div>
    <div class="formGroup">
            <label for="respository">Repository Link</label>
            <input type="text" name="respository" id="inputRepository" cols="30" rows="5"/>
    </div>
    <div class="formGroup">
            <label for="liveLink">Live Link</label>
            <input type="text" name="liveLink" id="inputLiveLink" cols="30" rows="5"/>
    </div>
`

const optionState = reactive({
    selectedOption: 0,
    options: [
        {
            name: "post",
            element: postOptions,
            apiRoute: "/api/v1/post"
        },
        {
            name: "series",
            element: seriesOptions,
            apiRoute: "/api/v1/series"
        },
        {
            name: "projects",
            element: projectOptions,
            apiRoute: "/api/v1/project"
        },
    ]
})

const onFormRequest = (e) => {
    e.detail.parameters['hx-post'] = optionState.options[optionState.selectedOption].apiRoute;
};

const onContentOptionChange = (e) => {
    var optionInt = optionState.selectedOption = parseInt(e.target.value);
    optionState.selectedOption = optionInt;
    const form = document.querySelector('form');
    form.addEventListener('htmx:configRequest', onFormRequest);
    //e.detail.parameters['hx-post'] = optionState.options[optionState.selectedOption].apiRoute;
    console.log(optionState.options[optionState.selectedOption].apiRoute)
    console.log(optionState.selectedOption)
}

watch(() => optionState.selectedOption, (selectedOption) => {
    optionState.options[selectedOption]
})

const contentForm = html`
    <form hx-post="${() => optionState.options[optionState.selectedOption].apiRoute}">
        <div class="formGroup">
            <label for="contentOption">Content Option</label>
            <select name="contentOption" id="contentOption" @change="${onContentOptionChange}">
                <option value=0>Post</option>
                <option value=1>Series</option>
                <option value=2>Project</option>
            </select>
        </div>
        ${() => optionState.options[optionState.selectedOption].element}
        <div class="formGroup">
            <button class="formButton" type="submit">Send</button>
            <button class="formButton" type="reset">Clear</button>
        </div>
    </form>
`

export default contentForm;
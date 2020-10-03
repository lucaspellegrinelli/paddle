import { shallowMount, createLocalVue } from '@vue/test-utils';
import InformesLista from '../../src/views/InformesLista.vue';

jest.mock("axios", () => ({
    get: () => Promise.resolve({ data : {
                conteudo : [{id : '1', titulo : 'titulo1', data : 'data1', corpo: 'corpo1'},
                  {id : '2', titulo : 'titulo2', data : 'data2', corpo: 'corpo2'},
                  {id : '3', titulo : 'titulo3', data : 'data3', corpo: 'corpo3'},
                  {id : '4', titulo : 'titulo4', data : 'data4', corpo: 'corpo4'},
                  {id : '5', titulo : 'titulo5', data : 'data5', corpo: 'corpo5'}]
                }})
  }))


describe('Testa InformesLista.vue', () => {
    
  it('Testa lista de posts', () => {
    var wrapper = shallowMount(InformesLista);

    //Testa se tem 5 posts
    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.posts.length).toBe(5);
    });    

    //Testa se tem 2 por página
    //Testa se mudou de página
    });

    it('Testa visibilidade do botão', () => {
      var wrapper = shallowMount(InformesLista);
  
      // testa se botão de novo informe não é exibido
      expect(wrapper.find('.novo-informe').exists()).toBeFalsy()
      });
})
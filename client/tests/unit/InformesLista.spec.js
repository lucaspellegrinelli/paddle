import { shallowMount } from '@vue/test-utils';
import InformesLista from '../../src/views/InformesLista.vue';
import Informe from '../../src/components/Informe.vue';

jest.mock("axios", () => ({
    get: () => Promise.resolve({ data : {
                conteudo : [{id : '1', titulo : 'titulo1', data : 'data1', corpo: 'corpo1'},
                  {id : '2', titulo : 'titulo2', data : 'data2', corpo: 'corpo2'},
                  {id : '3', titulo : 'titulo3', data : 'data3', corpo: 'corpo3'},
                  {id : '4', titulo : 'titulo4', data : 'data4', corpo: 'corpo4'},
                  {id : '5', titulo : 'titulo5', data : 'data5', corpo: 'corpo5'},
                  {id : '6', titulo : 'titulo6', data : 'data6', corpo: 'corpo6'}]
                }})
  }))

describe('Testa InformesLista.vue', () => {
  let wrapper;  
  beforeEach(() => {wrapper = shallowMount(InformesLista)});

  test('Testa se lista de posts está completa', () => {
    wrapper.vm.$nextTick(() => {
      expect(wrapper.vm.posts.length).toBe(6);
    });  
  });

  test('Testa se posts aparecem na página na ordem certa', () => {
    wrapper.vm.$nextTick(() => {
      informes = wrapper.findComponent(Informe);
      expect(informes).toHaveLength(5);
      expect(informes.at(0).props('post_info')).toBe('corpo1');
      expect(informes.at(1).props('post_info')).toBe('corpo2');
      expect(informes.at(4).props('post_info')).toBe('corpo5');
    });  
  });


  test('Testa paginação', () => {
    wrapper.setData({ pagina_atual: 2 })
    wrapper.vm.$nextTick(() => {
      informes = wrapper.findAllComponents(Informe);
      expect(informes).toHaveLength(1); //Testa se agora só tem 1 na página atual
      expect(informes.at(0).props('post_info')).toBe('corpo6'); //Testa se é o 6
    });
  });

  test('Testa visibilidade do botão', () => {
    //Testa se botão de novo informe não existe
    expect(wrapper.find('.novo-informe').exists()).toBeFalsy();

    //Testa se botão existe para o admin
    wrapper.vm.$root = { logado: true, admin:true };
    wrapper.vm.$nextTick(() => {
      expect(wrapper.find('.novo-informe').exists()).toBeTruthy();
    });
  });
})